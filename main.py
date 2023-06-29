from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity



movies_dataset_completo= pd.read_csv("../movies_dataset_completo.csv")

movies_dataset_recomendación=pd.read_csv('../movies_dataset_recomendación.csv')

app= FastAPI()

#http://127.0.0.1:8000

@app.get('/filmaciones_por_mes')
def cantidad_filmaciones_mes(mes):
    mes = mes.capitalize()
    Total_Películas = movies_dataset_completo.loc[movies_dataset_completo['Mes'] == mes].shape[0]
    return {'Mes':mes, 'Cantidad Totál de Películas':Total_Películas}


@app.get('/filmaciones_por_dia')
def cantidad_filmaciones_dia(dia):
    dia = dia.capitalize()    
    Total_Películas = movies_dataset_completo.loc[movies_dataset_completo['Día_Español'] == dia].shape[0]
    return {'Día':dia, 'Cantidad Totál de Películas':Total_Películas}


@app.get('/popularidad')
def score_titulo(titulo_de_la_filmacion):
    titulo_de_la_filmacion = titulo_de_la_filmacion.title()    
    
    pelicula = movies_dataset_completo.loc[movies_dataset_completo['title'] == titulo_de_la_filmacion]
    if pelicula.empty:
        return  "No se encontró la película."
    
    else:
        titulo = pelicula['title'].values[0]
        año_estreno = pelicula['release_year'].values[0]
        score = pelicula['popularity'].values[0]
        return f"La película {titulo} fue estrenada en el año {año_estreno} con un score de popularidad de {score}."
    
    
@app.get('/votacion')

def votos_titulo(titulo_de_la_filmacion):
    titulo_de_la_filmacion = titulo_de_la_filmacion.title()
    pelicula = movies_dataset_completo.loc[movies_dataset_completo['title'] == titulo_de_la_filmacion]
    
    if pelicula.empty:
        return "No se encontró la película."
    
    total_votos = pelicula['vote_count'].values[0]
    promedio_votos = pelicula['vote_average'].values[0]
    año_estreno = pelicula['release_year'].values[0]
    
    if total_votos >= 2000:
        return f"La película {titulo_de_la_filmacion} fue estrenada en el año {año_estreno}. La misma cuenta con un total de {total_votos} valoraciones, con un promedio de {promedio_votos}."
    else:
        return "La película no cumple con el requisito de tener al menos 2000 valoraciones."    
   
 
 
@app.get('/actor')  
def get_actor(nombre_actor):
    movies_dataset_completo['Reparto'] = movies_dataset_completo['Reparto'].fillna('')   
    actor = movies_dataset_completo[movies_dataset_completo['Reparto'].str.contains(nombre_actor, case=False)]
    cantidad_filmaciones = actor.shape[0]
    éxito = actor['return'].sum()
    promedio = éxito / cantidad_filmaciones if cantidad_filmaciones > 0 else 0

    return f"El actor {nombre_actor} ha participado de {cantidad_filmaciones} filmaciones. El mismo ha conseguido un retorno de {éxito} con un promedio de {promedio} por filmación"

@app.get('/director')
def get_director(nombre_director):
    movies_dataset_completo['Director'] = movies_dataset_completo['Director'].fillna('')
    
    director = movies_dataset_completo[movies_dataset_completo['Director'].str.contains(nombre_director, case=False)]
    if director.empty:
        return "No se encontraron películas del director."
    
    éxito = director['return'].sum()
    
    peliculas = director[['title', 'release_year', 'return', 'budget', 'revenue']].to_dict('records')

    return {
        'Éxito': éxito,
        'Películas': peliculas
    }
    
@app.get('/recomendación') 
def recomendacion(titulo):  
    
    
    pelicula_seleccionada = movies_dataset_recomendación[movies_dataset_recomendación['title'] == titulo]

    if pelicula_seleccionada.empty:
        return "No se encontró la película."

    #  matriz de simililitud entre películas para esto, usamos la fila de la peli sin el título y otras columnas qu eno necesito,
    #  además todo el dataset sin la columna tiítulo y las mismas columnas
    
    similitudes = cosine_similarity(pelicula_seleccionada.drop('title', axis=1), movies_dataset_recomendación.drop('title', axis=1))
    # accedemos con el argsort a las películas con similitud a la primera película que en este caso
    #  es la película que buscamos, y luego se seleccionan los útimos 5 índices (excluyendo la película
    # seleccionada) y por último se invierten los índices. 
    indices_similares = similitudes.argsort()[0][-6:-1][::-1]

    # finalmente obtenemos los títulos de las películas más similares y lo convertimos en lista
    peliculas_similares = movies_dataset_recomendación.iloc[indices_similares]['title'].tolist()

    return peliculas_similares  