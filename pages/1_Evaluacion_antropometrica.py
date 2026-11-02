import streamlit as st

# --------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# --------------------------------------------------

st.title("🌿 Evaluación antropométrica")
st.caption("Conoce algunos indicadores básicos de tu estado nutricional.")

st.markdown("""
Esta herramienta permite calcular el índice de masa corporal (IMC)
a partir del peso y la estatura.

*Importante:* el IMC es un indicador de cribado. No constituye
un diagnóstico médico ni sustituye una evaluación nutricional.
""")

st.divider()

# --------------------------------------------------
# FORMULARIO
# --------------------------------------------------

st.subheader("📝 Datos personales")

with st.form("formulario_antropometrico"):

    edad = st.number_input(
        "Edad (años)",
        min_value=20,
        max_value=120,
        value=20,
        step=1
    )

    peso = st.number_input(
        "Peso (kg)",
        min_value=0.1,
        max_value=500.0,
        value=60.0,
        step=0.1
    )

    estatura = st.number_input(
        "Estatura (cm)",
        min_value=50.0,
        max_value=250.0,
        value=160.0,
        step=0.1
    )

    calcular = st.form_submit_button(
        "Calcular mi IMC",
        use_container_width=True
    )

# --------------------------------------------------
# CÁLCULO E INTERPRETACIÓN
# --------------------------------------------------

if calcular:

    if peso <= 0 or estatura <= 0:
        st.error("Introduce un peso y una estatura válidos.")

    else:

        estatura_m = estatura / 100

        imc = peso / (estatura_m ** 2)

        st.divider()
        st.subheader("📊 Resultado de tu evaluación")

        st.metric(
            label="Índice de masa corporal (IMC)",
            value=f"{imc:.1f} kg/m²"
        )

        # Clasificación orientativa para adultos

        if imc < 18.5:
            clasificacion = "Bajo peso"
            explicacion = (
                "El resultado se encuentra por debajo del "
                "intervalo de referencia habitual para adultos."
            )

        elif imc < 25:
            clasificacion = "Intervalo de peso considerado normal"
            explicacion = (
                "El resultado se encuentra dentro del intervalo "
                "de referencia habitual para adultos."
            )

        elif imc < 30:
            clasificacion = "Sobrepeso"
            explicacion = (
                "El resultado se encuentra en el intervalo "
                "de sobrepeso según la clasificación del IMC."
            )

        elif imc < 35:
            clasificacion = "Obesidad clase I"
            explicacion = (
                "El resultado corresponde al intervalo de obesidad "
                "clase I según el IMC."
            )

        elif imc < 40:
            clasificacion = "Obesidad clase II"
            explicacion = (
                "El resultado corresponde al intervalo de obesidad "
                "clase II según el IMC."
            )

        else:
            clasificacion = "Obesidad clase III"
            explicacion = (
                "El resultado corresponde al intervalo de obesidad "
                "clase III según el IMC."
            )

        st.success(f"Clasificación orientativa: {clasificacion}")

        st.write(explicacion)

        st.info("""
        *¿Qué significa este resultado?*

        El IMC relaciona el peso con la estatura, pero no distingue
        entre masa muscular, masa grasa y otros componentes corporales.
        Por eso, debe interpretarse junto con otros datos clínicos y
        nutricionales.
        """)

        st.warning("""
        *Limitaciones*

        Este cálculo no es suficiente para diagnosticar desnutrición,
        sobrepeso u obesidad. Puede ser poco representativo en personas
        con gran masa muscular, edema, alteraciones de la composición
        corporal u otras condiciones especiales.
        """)

        st.caption(
            "Herramienta educativa de Yaritza AI. "
            "No sustituye la valoración de un profesional."
        )

# --------------------------------------------------
# INFORMACIÓN ADICIONAL
# --------------------------------------------------

st.divider()

with st.expander("¿Cómo se calcula el IMC?"):

    st.latex(r"IMC = \\frac{Peso\\ (kg)}{Estatura\\ (m)^2}")

    st.write("""
    Para adultos, la clasificación internacional habitual utiliza
    los siguientes intervalos:
    """)

    st.markdown("""
    - Menor de 18,5: bajo peso.
    - 18,5 a 24,9: intervalo considerado normal.
    - 25,0 a 29,9: sobrepeso.
    - 30,0 a 34,9: obesidad clase I.
    - 35,0 a 39,9: obesidad clase II.
    - 40,0 o más: obesidad clase III.
    """)
