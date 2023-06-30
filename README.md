![](https://imagizer.imageshack.com/img923/1593/Yw0c6j.png)

# <h1 align=center> **PROYECTO INDIVIDUAL ** </h1>
## Rol de un MLOps Engineer.
![](https://www.compunneldigital.com/wp-content/uploads/2022/08/MicrosoftTeams-image-115.png)

MLOps son un conjunto de prácticas que tienen como objetivo optimizar el proceso de ML y definir una transferencia fluida entre los científicos de datos y los ingenieros de ML a los modelos en producción de manera confiable y eficiente. El enfoque está diseñado para mejorar la calidad de los modelos de producción, mejorando así su viabilidad comercial mientras cumple con los requisitos reglamentarios.

El flujo de trabajo de MLOps atraviesa el ciclo de vida completo del modelo de aprendizaje automático, desde la creación hasta la implementación y la gobernanza continua a partir de entonces. Garantiza una evolución constante del modelo al contrarrestar los cambios y desviaciones emergentes. Esto permite a las empresas generar resultados procesables con precisión que pueden utilizar para tomar mejores decisiones.



## Objetivo del Proyecto
Llevar desde cero el proceso de un data engineer, pasando por disponibilizar los datos en una API,  hasta desarrollar un sistema de recomendación de películas por medio de la aplicación de un modelo de ML

## Partes del Proyecto

### 1. ETL:
En esta parte se extraen los datos de dos fuentes donde se encuentran la información de todas las películas con la que se va a trabajar, luego se realizan algunas tranformaciones según las necesidades que se tengan para luego cargarlas como un sistema de análisis.
### 2. Desarrollo de la API:
la idea aquí es disponibilizar los datos de la empresa por medio de la creación de 6 funciones para los endpoints en la API.
- FUNCIÓN1: Cantidad de películas estrenadas en el mes que se consulta.
- FUNCIÓN2: Cantidad de películas estrenadas en el Día que se consulta.
- FUNCIÓN3: Esta función devuelve el nombre de la película, el año de estreno y el puntaje de popularidad.
- FUNCIÓN4: Recibe el nombre de una película y devuelve la votación y el promedio.
- FUNCIÓN5:  Recibe el nombre de un actor  y devuelve la participación el número de películas en las que ha participado, además del retorno y el promedio por filmación.
- FUNCIÓN6: Recibe el nombre de un Director  y devuelve el éxito a través del retorno, además el nombre de cada película, con fecha de lanzamiento, retorno individual, costo y ganancia de esta.
Para esta parte se hizo uso de FastAPI
### 3. EDA: 
En el ETL se limpiaron y transformaron los datos pero ahora debemos obtener los datos  que se necesitan para que el modelo de ML sea un éxito. Entonces se deben preparar los datos, ver si necesitan alguna otra limpieza y convertirlos de alguna manera en características que ayudarán al modelo.
### 4. SISTEMA DE RECOMENDACIÓN: 
Se selecciona y entrena un modelo de machine learning apropiado. Para este proyecto se llevó a cabo un modelo basado en la similitud del coseno.
### 5. SISTEMA DE RECOMENDACIÓN: 
aquí se llega al proceso de poner en funcionamiento el sistema en un entorno de producción, donde los usuarios pueden acceder y utilizar las funcionalidades de recomendación. Esto se hizo con la ayuda de Render.
### 5. Deployment: 
Aquí se llega al proceso de poner en funcionamiento el sistema en un entorno de producción, donde los usuarios pueden acceder y utilizar las funcionalidades de recomendación. Esto se hizo con la ayuda de Render.
## Requerimientos para llevar a cabo este proyecto:
- pandas
- uvicorn
- scikit-learn
- matplotlib
- seaborn
- wordcloud
- missingno
- numpy

###  Link Render:
[Link Render](http://https://sebastian-figueroa-proyecto-i.onrender.com/docs "Link Render")
