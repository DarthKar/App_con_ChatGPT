import streamlit as st
import pandas as pd
import datetime as dt

# Inicializar datos
if "data" not in st.session_state:
    st.session_state.data = {
        "Fecha": [],
        "Categoría": [],
        "Monto": [],
        "Tipo": [],  # 'Ingreso' o 'Gasto'
        "Descripción": []
    }

# Función para agregar transacciones
def agregar_transaccion(fecha, categoria, monto, tipo, descripcion):
    st.session_state.data["Fecha"].append(fecha)
    st.session_state.data["Categoría"].append(categoria)
    st.session_state.data["Monto"].append(monto)
    st.session_state.data["Tipo"].append(tipo)
    st.session_state.data["Descripción"].append(descripcion)

# Configuración de la app
st.title("Gestor de Finanzas Personales")
st.write("Administra tus finanzas personales con facilidad.")

# Entrada de datos
st.header("Registrar Transacción")
col1, col2 = st.columns(2)

with col1:
    fecha = st.date_input("Fecha", dt.date.today())
    categoria = st.selectbox("Categoría", ["Alimentos", "Transporte", "Vivienda", "Entretenimiento", "Otros"])
    tipo = st.radio("Tipo", ["Ingreso", "Gasto"])

with col2:
    monto = st.number_input("Monto", min_value=0.0, step=0.01)
    descripcion = st.text_input("Descripción")

if st.button("Agregar"):
    agregar_transaccion(fecha, categoria, monto, tipo, descripcion)
    st.success("¡Transacción agregada!")

# Mostrar datos
st.header("Transacciones Registradas")
if st.session_state.data["Fecha"]:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)
else:
    st.write("No hay transacciones registradas.")

# Reportes
st.header("Reportes")
reporte_tipo = st.selectbox("Tipo de Reporte", ["Semanal", "Mensual"])
fecha_inicio = st.date_input("Fecha de Inicio", dt.date.today() - dt.timedelta(days=7))
fecha_fin = st.date_input("Fecha de Fin", dt.date.today())

if st.button("Generar Reporte"):
    if fecha_inicio > fecha_fin:
        st.error("La fecha de inicio no puede ser mayor que la fecha de fin.")
    else:
        df = pd.DataFrame(st.session_state.data)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        filtro = (df["Fecha"] >= pd.to_datetime(fecha_inicio)) & (df["Fecha"] <= pd.to_datetime(fecha_fin))
        df_filtrado = df[filtro]

        if df_filtrado.empty:
            st.write("No hay transacciones en el rango seleccionado.")
        else:
            ingresos = df_filtrado[df_filtrado["Tipo"] == "Ingreso"]["Monto"].sum()
            gastos = df_filtrado[df_filtrado["Tipo"] == "Gasto"]["Monto"].sum()
            balance = ingresos - gastos

            st.write(f"**Total Ingresos:** ${ingresos:.2f}")
            st.write(f"**Total Gastos:** ${gastos:.2f}")
            st.write(f"**Balance:** ${balance:.2f}")
            st.dataframe(df_filtrado)

# Presupuesto y metas de ahorro
st.header("Presupuesto y Metas de Ahorro")
col1, col2 = st.columns(2)

with col1:
    presupuesto = st.number_input("Presupuesto Mensual", min_value=0.0, step=0.01)
    ahorro_meta = st.number_input("Meta de Ahorro Mensual", min_value=0.0, step=0.01)

if st.button("Calcular Desempeño"):
    gastos_totales = pd.DataFrame(st.session_state.data).query("Tipo == 'Gasto'")["Monto"].sum()
    presupuesto_restante = presupuesto - gastos_totales
    ahorro_real = presupuesto_restante if presupuesto_restante > 0 else 0

    st.write(f"**Presupuesto Restante:** ${presupuesto_restante:.2f}")
    st.write(f"**Meta de Ahorro:** ${ahorro_meta:.2f}")
    st.write(f"**Ahorro Real:** ${ahorro_real:.2f}")

    if ahorro_real >= ahorro_meta:
        st.success("¡Estás cumpliendo tu meta de ahorro!")
    else:
        st.warning("No estás cumpliendo tu meta de ahorro.")
