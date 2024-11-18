import streamlit as st
import requests

# Función para obtener la información del juego
def obtener_info_juego(nombre_juego):
    url = f'https://api.rawg.io/api/games'
    params = {'key': 'tu_api_key', 'page_size': 1, 'search': nombre_juego}
    response = requests.get(url, params=params)
    data = response.json()

    if data['results']:
        juego = data['results'][0]
        descripcion = juego.get('description', 'Descripción no disponible.')
        generos = ', '.join([genero['name'] for genero in juego.get('genres', [])])
        año_lanzamiento = juego.get('released', 'Año no disponible.')
        calificacion = juego.get('rating', 'No disponible')
        plataformas = ', '.join([plataforma['platform']['name'] for plataforma in juego.get('platforms', [])])
        enlace = juego.get('website', 'No disponible')

        return {
            'descripcion': descripcion,
            'generos': generos,
            'año_lanzamiento': año_lanzamiento,
            'calificacion': calificacion,
            'plataformas': plataformas,
            'enlace': enlace,
        }
    else:
        return None

# Título y label con tu nombre
st.title('Consulta de Videojuegos')
st.write('Esta app fue desarrollada por Miguel Angel Peña Marin')

# Input del nombre del juego
nombre_juego = st.text_input('Ingresa el nombre del juego:')

if nombre_juego:
    info_juego = obtener_info_juego(nombre_juego)

    if info_juego:
        st.subheader('Información del Juego')
        
        # Columnas para un diseño más limpio
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**Nombre del juego:** {nombre_juego}")
            st.markdown(f"**Géneros:** {info_juego['generos']}")
            st.markdown(f"**Año de lanzamiento:** {info_juego['año_lanzamiento']}")
            st.markdown(f"**Plataformas:** {info_juego['plataformas']}")

        with col2:
            st.markdown(f"**Calificación promedio:** {info_juego['calificacion']}")
            if info_juego['enlace'] != 'No disponible':
                st.markdown(f"[**Sitio oficial**]({info_juego['enlace']})")

        # Mostrar descripción en un área expandible
        with st.expander('Descripción del Juego'):
            st.write(info_juego['descripcion'])
    else:
        st.error('Juego no encontrado. Por favor, intenta con otro nombre.')
