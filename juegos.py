import streamlit as st
import requests

# Función para obtener la información del juego
def obtener_info_juego(nombre_juego):
    url = 'https://api.rawg.io/api/games'
    params = {'key': '10353b6967544f359fae182090a15b06', 'page_size': 1, 'search': nombre_juego}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None, "Error al conectar con la API."

    data = response.json()
    if "results" in data and data["results"]:
        juego = data["results"][0]
        descripcion = juego.get("description", "Descripción no disponible")
        generos = ", ".join([genero["name"] for genero in juego.get("genres", [])])
        año_lanzamiento = juego.get("released", "Fecha de lanzamiento no disponible")
        desarrolladores = ", ".join(
            [dev["name"] for dev in juego.get("developers", [])]
        ) if "developers" in juego else "No disponible"
        plataformas = ", ".join(
            [plataforma["platform"]["name"] for plataforma in juego.get("platforms", [])]
        ) if "platforms" in juego else "No disponible"
        return {
            "descripcion": descripcion,
            "generos": generos,
            "año_lanzamiento": año_lanzamiento,
            "desarrolladores": desarrolladores,
            "plataformas": plataformas,
        }, None
    else:
        return None, "Juego no encontrado."

# Título y label con tu nombre
st.title("Consulta de Videojuegos")
st.write("Esta app fue desarrollada por Miguel Angel Peña Marin")

# Input del nombre del juego
nombre_juego = st.text_input("Ingresa el nombre del juego:")

if nombre_juego:
    info_juego, error = obtener_info_juego(nombre_juego)

    if error:
        st.error(error)
    else:
        st.subheader("Información del Juego:")
        st.write(f"**Descripción:** {info_juego['descripcion']}")
        st.write(f"**Géneros:** {info_juego['generos']}")
        st.write(f"**Año de Lanzamiento:** {info_juego['año_lanzamiento']}")
        st.write(f"**Desarrolladores:** {info_juego['desarrolladores']}")
        st.write(f"**Plataformas:** {info_juego['plataformas']}")
