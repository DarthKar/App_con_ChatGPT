import streamlit as st
import pandas as pd
import datetime as dt

# Inicialización de los datos en session_state
if "finanzas" not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(
        columns=["Fecha", "Categoría", "Monto", "Tipo", "Descripción"]
    )

# Función para agregar transacciones
def agregar_transaccion(fecha, categoria, monto, tipo, descripcion):
    nueva_transaccion = pd.DataFrame(
        {
            "Fecha": [fecha],
            "Categoría": [categoria],
            "Monto": [monto],
            "Tipo": [tipo],
            "Descripción": [descripcion],
        }
    )
    st.session_state.finanzas = pd.concat(
        [st.session_state.finanzas, nueva_transaccion], ignore_index=True
    )

# Título de la app
st.title("Gestor de Finanzas Personales")
st.write("Esta app fue desarrollada por Miguel Ángel Peña Marín")

# Registro de transacciones
st.header("Registrar Transacción")
col1, col2 = st.columns(2)

with col1:
    fecha = st.date_input("Fecha", dt.date.today())
    categoria = st.selectbox(
        "Categoría", ["Alimentos", "Transporte", "Vivienda", "Entretenimiento", "Otros"]
    )
    tipo = st.radio("Tipo de Transacción", ["Ingreso", "Gasto"])

with col2:
    monto = st.number_input("Monto ($)", min_value=0.0, step=0.01)
    descripcion = st.text_input("Descripción")

if st.button("Agregar Transacción"):
    agregar_transaccion(fecha, categoria, monto, tipo, descripcion)
    st.success("¡Transacción agregada exitosamente!")

# Mostrar las transacciones registradas
st.header("Transacciones Registradas")
if not st.session_state.finanzas.empty:
    st.dataframe(st.session_state.finanzas)
else:
    st.write("No hay transacciones registradas.")

# Generación de reportes
st.header("Generar Reportes")
reporte_tipo = st.selectbox("Selecciona el tipo de reporte", ["Semanal", "Mensual"])
fecha_inicio = st.date_input("Fecha de Inicio", dt.date.today() - dt.timedelta(days=7))
fecha_fin = st.date_input("Fecha de Fin", dt.date.today())

if st.button("Generar Reporte"):
    if fecha_inicio > fecha_fin:
        st.error("La fecha de inicio no puede ser mayor que la fecha de fin.")
    else:
        # Convertir las fechas de inicio y fin al tipo datetime
        fecha_inicio = pd.to_datetime(fecha_inicio)
        fecha_fin = pd.to_datetime(fecha_fin)
        
        # Asegurarse de que las fechas en el DataFrame sean del tipo datetime
        df = st.session_state.finanzas.copy()
        df["Fecha"] = pd.to_datetime(df["Fecha"])

        # Filtrar las transacciones por el rango de fechas
        filtro = (df["Fecha"] >= fecha_inicio) & (df["Fecha"] <= fecha_fin)
        df_filtrado = df[filtro]

        if df_filtrado.empty:
            st.warning("No hay transacciones en el rango seleccionado.")
        else:
            ingresos = df_filtrado[df_filtrado["Tipo"] == "Ingreso"]["Monto"].sum()
            gastos = df_filtrado[df_filtrado["Tipo"] == "Gasto"]["Monto"].sum()
            balance = ingresos - gastos

            st.subheader("Resumen del Reporte")
            st.write(f"**Total de Ingresos:** ${ingresos:.2f}")
            st.write(f"**Total de Gastos:** ${gastos:.2f}")
            st.write(f"**Balance:** ${balance:.2f}")
            st.write("**Detalle de Transacciones:**")
            st.dataframe(df_filtrado)

# Presupuesto y metas de ahorro
st.header("Presupuesto y Metas de Ahorro")
presupuesto = st.number_input("Presupuesto Mensual ($)", min_value=0.0, step=0.01)
meta_ahorro = st.number_input("Meta de Ahorro Mensual ($)", min_value=0.0, step=0.01)

if st.button("Calcular Desempeño"):
    gastos_totales = st.session_state.finanzas.query("Tipo == 'Gasto'")["Monto"].sum()
    presupuesto_restante = presupuesto - gastos_totales
    ahorro_real = max(0, presupuesto_restante)

    st.subheader("Resultados")
    st.write(f"**Presupuesto Restante:** ${presupuesto_restante:.2f}")
    st.write(f"**Meta de Ahorro:** ${meta_ahorro:.2f}")
    st.write(f"**Ahorro Real:** ${ahorro_real:.2f}")

    if ahorro_real >= meta_ahorro:
        st.success("¡Felicidades! Estás cumpliendo con tu meta de ahorro.")
    else:
        st.warning("No estás alcanzando tu meta de ahorro.")
