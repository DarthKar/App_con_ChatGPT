import streamlit as st
import pandas as pd

# Inicialización de los datos en session_state
if "materias" not in st.session_state:
    st.session_state.materias = pd.DataFrame(
        columns=["Materia", "Calificación", "Créditos", "Tipología"]
    )

# Función para agregar una nueva materia
def agregar_materia(materia, calificacion, creditos, tipologia):
    nueva_materia = pd.DataFrame(
        {
            "Materia": [materia],
            "Calificación": [calificacion],
            "Créditos": [creditos],
            "Tipología": [tipologia]
        }
    )
    st.session_state.materias = pd.concat(
        [st.session_state.materias, nueva_materia], ignore_index=True
    )

# Cálculo del PAPA
def calcular_papa(df):
    # Cálculo global
    df["Producto"] = df["Calificación"] * df["Créditos"]
    total_productos = df["Producto"].sum()
    total_creditos = df["Créditos"].sum()
    papa_global = total_productos / total_creditos if total_creditos != 0 else 0

    # Cálculo por tipología
    papa_tipologia = {}
    for tipologia in df["Tipología"].unique():
        df_tipologia = df[df["Tipología"] == tipologia]
        total_productos_tipologia = df_tipologia["Producto"].sum()
        total_creditos_tipologia = df_tipologia["Créditos"].sum()
        papa_tipologia[tipologia] = total_productos_tipologia / total_creditos_tipologia if total_creditos_tipologia != 0 else 0

    return papa_global, papa_tipologia

# Título de la app
st.title("Calculadora del Promedio Aritmético Ponderado Acumulado (PAPA)")
st.write("Esta app fue desarrollada por Miguel Ángel Peña Marín")

# Agregar una materia
st.header("Agregar Materia")
col1, col2, col3 = st.columns(3)

with col1:
    materia = st.text_input("Nombre de la materia")
with col2:
    calificacion = st.number_input("Calificación", min_value=0.0, max_value=5.0, step=0.1)
with col3:
    creditos = st.number_input("Créditos", min_value=1, step=1)

tipologia = st.selectbox("Tipología de la asignatura", ["Teoría", "Prácticas", "Electiva", "Optativa"])

if st.button("Agregar Materia"):
    if materia and calificacion >= 0 and creditos > 0:
        agregar_materia(materia, calificacion, creditos, tipologia)
        st.success("¡Materia agregada exitosamente!")
    else:
        st.error("Por favor, ingresa todos los datos correctamente.")

# Mostrar las materias registradas
st.header("Materias Registradas")
if not st.session_state.materias.empty:
    st.dataframe(st.session_state.materias)
else:
    st.write("No hay materias registradas.")

# Calcular el PAPA Global
if st.button("Calcular PAPA Global"):
    if not st.session_state.materias.empty:
        papa_global, _ = calcular_papa(st.session_state.materias)

        st.subheader("PAPA Global")
        st.write(f"**PAPA Global:** {papa_global:.2f}")
    else:
        st.error("No hay materias registradas para calcular el PAPA global.")

# Calcular el PAPA por Tipología
st.header("Calcular PAPA por Tipología")
tipologia_seleccionada = st.selectbox("Selecciona la Tipología", st.session_state.materias["Tipología"].unique())
if st.button("Calcular PAPA por Tipología"):
    if not st.session_state.materias.empty:
        _, papa_tipologia = calcular_papa(st.session_state.materias)
        
        if tipologia_seleccionada in papa_tipologia:
            st.subheader(f"PAPA para {tipologia_seleccionada}")
            st.write(f"**PAPA para {tipologia_seleccionada}:** {papa_tipologia[tipologia_seleccionada]:.2f}")
        else:
            st.error(f"No se encontraron materias para la tipología {tipologia_seleccionada}.")
    else:
        st.error("No hay materias registradas para calcular el PAPA por tipología.")
