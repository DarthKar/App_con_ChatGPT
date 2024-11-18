import streamlit as st
import requests

# Clave de la API (reemplázala con tu propia clave)
API_KEY = "10353b6967544f359fae182090a15b06"

# Función para buscar juegos
def buscar_juegos(nombre_juego):
    url = f"https://api.rawg.io/api/games"
    params = {"key": API_KEY, "search": nombre_juego, "page_size": 5}  # Devuelve hasta 5 resultados
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return None, "Error al conectar con la API."

    data = response.json()
    if "results" in data and data["results"]:
        return data["results"], None
    else:
        return None, "No se encontraron resultados."

# Función para obtener detalles del juego
def obtener_detalles_juego(id_juego):
    url = f"https://api.rawg.io/api/games/{id_juego}"
    params = {"key": API_KEY}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return None, "Error al obtener los detalles del juego."

    data = response.json()
    return data, None

# Título y label con tu nombre
st.title("Consulta de Videojuegos")
st.write("Esta app fue desarrollada por Miguel Angel Peña Marin")

# Input del nombre del juego
nombre_juego = st.text_input("Ingresa el nombre del juego para buscar:")

if nombre_juego:
    juegos, error = buscar_juegos(nombre_juego)
    
    if error:
        st.error(error)
    else:
        st.subheader("Resultados de la búsqueda:")
        opciones = {juego["id"]: juego["name"] for juego in juegos}
        seleccion_id = st.selectbox("Selecciona un juego para ver más detalles:", opciones.keys(), format_func=lambda x: opciones[x])

        if seleccion_id:
            detalles, error_detalles = obtener_detalles_juego(seleccion_id)

            if error_detalles:
                st.error(error_detalles)
            else:
                st.subheader(f"Detalles del juego: {detalles['name']}")
                st.write(f"**Géneros:** {', '.join([g['name'] for g in detalles.get('genres', [])])}")
                st.write(f"**Año de lanzamiento:** {detalles.get('released', 'No disponible')}")
                st.write(f"**Desarrolladores:** {', '.join([dev['name'] for dev in detalles.get('developers', [])])}")
                st.write(f"**Plataformas:** {', '.join([plat['platform']['name'] for plat in detalles.get('platforms', [])])}")
                st.write(f"**Metacritic:** {detalles.get('metacritic', 'No disponible')}")
                st.image(detalles.get("background_image", ""), caption="Imagen del juego")
