import streamlit as st
import requests

# Función para obtener la información del juego
def obtener_info_juego(nombre_juego):
    url = f'https://api.rawg.io/api/games'
    params = {'key': '10353b6967544f359fae182090a15b06', 'page_size': 1, 'search': nombre_juego}
    response = requests.get(url, params=params)
    data = response.json()

    if data['results']:
        juego = data['results'][0]
        descripcion = juego.get('description', 'No disponible')
        generos = ', '.join([genero['name'] for genero in juego.get('genres', [])])
        año_lanzamiento = juego.get('released', 'No disponible')

        return descripcion, generos, año_lanzamiento
    else:
        return 'Juego no encontrado', '', ''

# Título y label con tu nombre
st.title('Consulta de Videojuegos')
st.write('Esta app fue desarrollada por Miguel Angel Peña Marin')

# Input del nombre del juego
nombre_juego = st.text_input('Ingresa el nombre del juego:')

if nombre_juego:
    descripcion, generos, año_lanzamiento = obtener_info_juego(nombre_juego)

    st.subheader('Descripción del Juego:')
    st.write(descripcion)

    st.subheader('Géneros:')
    st.write(generos)

    st.subheader('Año de Lanzamiento:')
    st.write(año_lanzamiento)
