import streamlit as st
from openai import OpenAI

# CONFIGURACION DE LA PAGINA
st.set_page_config(
    page_title="Yaritza AI",
    page_icon="🥗",
    layout="centered"
)

# IDENTIDAD DE YARITZA AI
INSTRUCCIONES = """
Eres Yaritza AI, un asistente de inteligencia artificial
especializado en educacion y orientacion nutricional.

Tu mision es proporcionar informacion cientifica,
comprensible, responsable y actualizada.

TUS AREAS DE CONOCIMIENTO SON:

1. Desnutricion y malnutricion.
2. Sobrepeso y obesidad.
3. Deficiencias de vitaminas y minerales.
4. Macronutrientes y micronutrientes.
5. Alimentacion equilibrada.
6. Habitos alimentarios.
7. Evaluacion nutricional educativa.
8. Prevencion de enfermedades relacionadas
   con la nutricion.

REGLAS:

- Responde siempre en español.
- Explica los terminos medicos.
- Utiliza informacion cientifica.
- No inventes resultados ni referencias.
- No establezcas diagnosticos definitivos.
- No prescribas medicamentos.
- No recomiendes suplementos sin valoracion profesional.
- No recomiendes dietas extremas.
- Solicita solamente los datos necesarios.
- No solicites nombres, cedulas ni direcciones.
- Explica las limitaciones de las mediciones.

SEGURIDAD:

Si el usuario presenta desmayos, confusion,
dificultad respiratoria, incapacidad para alimentarse
o signos de deshidratacion grave, recomienda
atencion medica urgente.

No sustituyas la consulta de un medico o nutricionista.

FORMATO DE RESPUESTA:

Cuando sea apropiado, organiza la informacion en:

1. Definicion.
2. Fisiopatologia.
3. Causas.
4. Manifestaciones.
5. Consecuencias.
6. Prevencion.
7. Cuando buscar atencion profesional.

Adapta la extension a la pregunta del usuario.
"""

# CONEXION CON LA API
cliente = None

try:
    api_key = st.secrets["OPENAI_API_KEY"]
    modelo = st.secrets.get("OPENAI_MODEL", "gpt-6-astra")
    cliente = OpenAI(api_key=api_key)

except Exception:
    st.error(
        "No se ha configurado correctamente la API. "
        "Revisa el archivo secrets.toml."
    )

# ENCABEZADO
st.title("🥗 Yaritza AI")

st.subheader(
    "Tu asistente inteligente de salud nutricional"
)

st.write(
    "Un espacio para aprender, comprender y mejorar "
    "tus conocimientos sobre nutricion y salud."
)

st.info(
    "Yaritza AI ofrece informacion educativa. "
    "No sustituye la valoracion de profesionales de salud."
)

# BOTON PARA LIMPIAR CONVERSACION
if st.button("Nueva conversacion"):
    st.session_state.messages = []
    st.rerun()

# HISTORIAL
if "messages" not in st.session_state:
    st.session_state.messages = []

# MOSTRAR CONVERSACION
for mensaje in st.session_state.messages:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# CAMPO PARA ESCRIBIR
pregunta = st.chat_input(
    "Escribe tu pregunta sobre nutricion..."
)

if pregunta:

    st.session_state.messages.append({
        "role": "user",
        "content": pregunta
    })

    with st.chat_message("user"):
        st.markdown(pregunta)

    if cliente is None:

        st.error(
            "No hay conexion con la inteligencia artificial. "
            "Revisa tu configuracion."
        )

    else:

        try:
            with st.chat_message("assistant"):

                with st.spinner("Yaritza AI esta pensando..."):

                    respuesta = cliente.responses.create(
                        model=modelo,
                        instructions=INSTRUCCIONES,
                        input=st.session_state.messages[-12:],
                        max_output_tokens=800
                    )

                    texto = respuesta.output_text

                    st.markdown(texto)

            st.session_state.messages.append({
                "role": "assistant",
                "content": texto
            })

        except Exception as error:

            st.error(
                "No se pudo generar la respuesta. "
                "Comprueba tu conexion, API Key y modelo."
            )

            st.caption(str(error))

# PIE DE PAGINA
st.divider()

st.caption(
    "Yaritza AI | Educacion y orientacion nutricional"
)

st.caption(
    "La informacion no constituye un diagnostico medico."
)