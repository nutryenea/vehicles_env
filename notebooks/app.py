# Importar las librerías
import pandas as pd
import plotly.express as px
import streamlit as st

# Leer archivo csv
car_data = pd.read_csv(
    '/Users/arturoparrasolano/Documents/Data_Science/vehicles_us.csv')

# Crear el encabezado de la app web
st.header('Análisis exploratorio de datos de anuncios de venta de coches')

# Mostrar el conjunto de datos en una tabla interactiva
st.subheader('Tabla de conjunto de datos')
st.dataframe(car_data)

# Crear encabezado para histograma
st.header('Construir histograma')

# Extraer el fabricante de la columna 'model' y crear la columna 'manufacturer'
car_data['manufacturer'] = [manufacturer.split()[0]
                            for manufacturer in car_data['model']]

# Crear botón para mostrar histograma
build_hist_button = st.checkbox(
    'Conteo de vehículos por fabricante y por tipo')

# Al hacer clic en el botón
if build_hist_button:
    # Crear un mensaje
    st.write(
        'Número de vehículos por fabricante y tipo')
    # Agrupar los datos por fabricante y tipo y contar
    manufacturer_type_count = car_data.groupby(
        ['manufacturer', 'type']).size().reset_index(name='count')

    # Crear histograma
    fig = px.bar(manufacturer_type_count,
                 x='manufacturer',
                 y='count',
                 color='type',
                 title='Distribución de vehículos por fabricante y tipo',
                 labels={'manufacturer': 'Fabricante', 'count': 'Cantidad', 'type': 'tipo'})
    # Mostrar gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Agrega otro botón que, al hacer clic en él, construya un gráfico de dispersión plotly-express. Nuevamente, considera utilizar las funciones st.write() y st.plotly_chart()

# Crear botón para mostrar gráfico de dispersión:
build_scatter_button = st.checkbox('Construir gráfico de dispersión')

# Al hacer clic en el botón:
if build_scatter_button:
    # Crear un mensaje
    st.write('Comparar relación entre precio y kilometraje')
    # Crear gráfico de dispersión
    fig = px.scatter(car_data,
                     x='odometer',
                     y='price',
                     color='manufacturer',
                     title='Relación entre precio y kilometraje',
                     labels={'odometer': 'Kilometraje', 'price': 'Precio'},
                     # Mostrar detalles al pasar el mouse
                     hover_data=['model', 'manufacturer', 'price'],
                     opacity=0.7)
    # Mostrar gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
