import streamlit as st
import numpy as np

# Función para simular el lanzamiento del dado
def lanzar_dado(num_lanzamientos=20):
    # Simular el lanzamiento de un dado de 6 caras num_lanzamientos veces
    return np.random.randint(1, 7, num_lanzamientos)

# Función para calcular las métricas estadísticas
def calcular_estadisticas(resultados):
    media = np.mean(resultados)
    mediana = np.median(resultados)
    
    # Calcular la moda utilizando np.unique() y buscando el valor más frecuente
    valores, conteo = np.unique(resultados, return_counts=True)
    moda = valores[np.argmax(conteo)]
    
    varianza = np.var(resultados)
    desviacion_estandar = np.std(resultados)
    
    return media, mediana, moda, varianza, desviacion_estandar

# Título de la aplicación
st.title("Simulación de Lanzamiento de un Dado")

# Descripción de la aplicación
st.write("""
    Esta aplicación simula el lanzamiento de un dado de seis caras veinte veces.
    Luego, muestra los resultados obtenidos y un análisis estadístico.
""")

# Simular el lanzamiento del dado
resultados = lanzar_dado()

# Mostrar los resultados del lanzamiento
st.write("### Resultados de los Lanzamientos:")
st.write(resultados)

# Calcular las métricas estadísticas
media, mediana, moda, varianza, desviacion_estandar = calcular_estadisticas(resultados)

# Mostrar los análisis estadísticos
st.write("### Análisis Estadístico:")
st.write(f"**Media:** {media:.2f}")
st.write(f"**Mediana:** {mediana}")
st.write(f"**Moda:** {moda}")
st.write(f"**Varianza:** {varianza:.2f}")
st.write(f"**Desviación Estándar:** {desviacion_estandar:.2f}")

# Calcular y mostrar la tabla de frecuencias
frecuencias = {i: np.count_nonzero(resultados == i) for i in range(1, 7)}

# Crear la tabla de frecuencias
st.write("### Tabla de Frecuencias:")
st.write(f"Frecuencia de cada número del dado:")
frecuencia_array = np.array([frecuencias[i] for i in range(1, 7)])

# Mostrar la tabla de frecuencias
tabla_frecuencias = np.column_stack([np.arange(1, 7), frecuencia_array])
st.write(tabla_frecuencias)

