import streamlit as st

# Título de la app
st.title("Conversor de Unidades")

# Autor de la app
st.write("Esta app fue elaborada por Miguel Angel Peña Marin.")

# Funciones de conversión
def convertir_temperatura(valor, tipo):
    if tipo == "Celsius a Fahrenheit":
        return valor * 9 / 5 + 32
    elif tipo == "Fahrenheit a Celsius":
        return (valor - 32) * 5 / 9
    elif tipo == "Celsius a Kelvin":
        return valor + 273.15
    elif tipo == "Kelvin a Celsius":
        return valor - 273.15


def convertir_longitud(valor, tipo):
    if tipo == "Pies a metros":
        return valor * 0.3048
    elif tipo == "Metros a pies":
        return valor / 0.3048
    elif tipo == "Pulgadas a centímetros":
        return valor * 2.54
    elif tipo == "Centímetros a pulgadas":
        return valor / 2.54


def convertir_peso(valor, tipo):
    if tipo == "Libras a kilogramos":
        return valor * 0.453592
    elif tipo == "Kilogramos a libras":
        return valor / 0.453592
    elif tipo == "Onzas a gramos":
        return valor * 28.3495
    elif tipo == "Gramos a onzas":
        return valor / 28.3495


def convertir_volumen(valor, tipo):
    if tipo == "Galones a litros":
        return valor * 3.78541
    elif tipo == "Litros a galones":
        return valor / 3.78541
    elif tipo == "Pulgadas cúbicas a centímetros cúbicos":
        return valor * 16.3871
    elif tipo == "Centímetros cúbicos a pulgadas cúbicas":
        return valor / 16.3871


def convertir_tiempo(valor, tipo):
    if tipo == "Horas a minutos":
        return valor * 60
    elif tipo == "Minutos a segundos":
        return valor * 60
    elif tipo == "Días a horas":
        return valor * 24
    elif tipo == "Semanas a días":
        return valor * 7


def convertir_velocidad(valor, tipo):
    if tipo == "Millas por hora a kilómetros por hora":
        return valor * 1.60934
    elif tipo == "Kilómetros por hora a metros por segundo":
        return valor / 3.6
    elif tipo == "Nudos a millas por hora":
        return valor * 1.15078
    elif tipo == "Metros por segundo a pies por segundo":
        return valor * 3.28084


def convertir_area(valor, tipo):
    if tipo == "Metros cuadrados a pies cuadrados":
        return valor * 10.7639
    elif tipo == "Pies cuadrados a metros cuadrados":
        return valor / 10.7639
    elif tipo == "Kilómetros cuadrados a millas cuadradas":
        return valor * 0.386102
    elif tipo == "Millas cuadradas a kilómetros cuadrados":
        return valor / 0.386102


def convertir_energia(valor, tipo):
    if tipo == "Julios a calorías":
        return valor / 4.184
    elif tipo == "Calorías a kilojulios":
        return valor * 4.184 / 1000
    elif tipo == "Kilovatios-hora a megajulios":
        return valor * 3.6
    elif tipo == "Megajulios a kilovatios-hora":
        return valor / 3.6


def convertir_presion(valor, tipo):
    if tipo == "Pascales a atmósferas":
        return valor / 101325
    elif tipo == "Atmósferas a pascales":
        return valor * 101325
    elif tipo == "Barras a libras por pulgada cuadrada":
        return valor * 14.5038
    elif tipo == "Libras por pulgada cuadrada a bares":
        return valor / 14.5038


def convertir_tamano_datos(valor, tipo):
    if tipo == "Megabytes a gigabytes":
        return valor / 1024
    elif tipo == "Gigabytes a Terabytes":
        return valor / 1024
    elif tipo == "Kilobytes a megabytes":
        return valor / 1024
    elif tipo == "Terabytes a petabytes":
        return valor / 1024


# Mapeo explícito entre categorías y funciones
funciones_conversion = {
    "Temperatura": convertir_temperatura,
    "Longitud": convertir_longitud,
    "Peso/Masa": convertir_peso,
    "Volumen": convertir_volumen,
    "Tiempo": convertir_tiempo,
    "Velocidad": convertir_velocidad,
    "Área": convertir_area,
    "Energía": convertir_energia,
    "Presión": convertir_presion,
    "Tamaño de Datos": convertir_tamano_datos
}

# Menú de selección
categoria = st.selectbox(
    "Selecciona una categoría de conversión:",
    [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de Datos"
    ]
)

if categoria:
    opciones = {
        "Temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
        "Longitud": ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"],
        "Peso/Masa": ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"],
        "Volumen": ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"],
        "Tiempo": ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"],
        "Velocidad": ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"],
        "Área": ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"],
        "Energía": ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"],
        "Presión": ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"],
        "Tamaño de Datos": ["Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
    }

    conversion = st.selectbox("Selecciona una conversión:", opciones[categoria])
    valor = st.number_input("Introduce el valor a convertir:", min_value=0.0, step=0.01)

    if st.button("Convertir"):
        funcion_conversion = funciones_conversion[categoria]
        resultado = funcion_conversion(valor, conversion)
        st.write(f"El resultado de la conversión es: {resultado}")
