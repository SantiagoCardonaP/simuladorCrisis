import streamlit as st
from PIL import Image
import base64
import io
import time

# =========================
# CONFIGURACIÓN DE PÁGINA
# =========================
st.set_page_config(
    page_title="Simulador de riesgo reputacional",
    page_icon="🟠",
    layout="centered"
)

# =========================
# FUNCIONES AUXILIARES
# =========================
def image_to_base64(image_path):
    img = Image.open(image_path)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def render_top_logo():
    logo_path = "logo-julius.png"
    try:
        img_b64 = image_to_base64(logo_path)
        st.markdown(
            f"""
            <div style='display:flex; justify-content:center; margin-top: 6px; margin-bottom: 10px;'>
                <img src="data:image/png;base64,{img_b64}" width="155px"/>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        st.markdown(
            "<div style='text-align:center; color:white; font-weight:700; margin-top:10px;'>Julius</div>",
            unsafe_allow_html=True
        )

def render_comfama_logo():
    comfama_logo_url = (
        "https://www.comfama.com/servicio-de-empleo/_gatsby/image/"
        "c5db45b591a70aadee27dc99cc568772/ac9159c9c186998eda3ce1ef38d6e292/"
        "logo_comfama.webp?u=https%3A%2F%2Fimages.ctfassets.net%2F203frbsx1z3n%2F"
        "2QY4vQqWGmpccWpnlVDJs2%2F6ec2ad2d8abede6605c917820904118d%2Flogo_comfama.png"
        "&a=w%3D650%26h%3D216%26fm%3Dwebp%26q%3D85&cd=2025-12-17T16%3A25%3A35.387Z"
    )
    st.markdown(
        f"""
        <div style='display:flex; justify-content:center; margin-bottom: 30px;'>
            <img src="{comfama_logo_url}" width="235px"/>
        </div>
        """,
        unsafe_allow_html=True
    )

def get_profile_analysis(profile):
    analyses = {
        "@tamtenenbaum": {
            "level": "Amarillo rojizo",
            "color": "#D96C1A",
            "content": """
**Tamara Tenenbaum**

Tenenbaum tiene una voz muy potente, contemporánea y atractiva para públicos urbanos, culturales y progresistas. Sus temas recurrentes incluyen feminismo, amor, deseo, autonomía, vínculos, familia y vida intelectual; ella misma explica el feminismo como una herramienta para pensar la relación entre lo público y lo privado.

**Riesgo principal para Comfama:** no es de reputación personal deteriorada, sino de encuadre ideológico. Para públicos conservadores o ya predispuestos a leer a Comfama como actor cultural “sesgado”, Tenenbaum es la que con más facilidad puede ser convertida en símbolo de agenda de género, sexualidad o élite intelectual. Ese riesgo aumenta precisamente porque tiene una voz clara, visible y reconocible.

**Brechas que podría exacerbar si se gestiona mal:**
- **Favorabilidad:** por rechazo de sectores que no lean el contenido, sino el símbolo.
- **Adaptación:** si Comfama no demuestra sensibilidad con públicos especiales o territorios diversos.
- **Empatía:** si el tono de la pieza promocional se percibe como doctrinario, sofisticado en exceso o poco inclusivo.

**Lectura táctica:** es útil si el objetivo es posicionar a Comfama como actor cultural contemporáneo y valiente, pero exige blindaje narrativo fuerte. No la usaría en un momento de sensibilidad reputacional alta ni en una campaña que necesite consenso amplio.
"""
        },
        "@alexkohan": {
            "level": "Amarillo",
            "color": "#D4B000",
            "content": """
**Alexandra Kohan**

Kohan ocupa un lugar interesante porque combina densidad intelectual con una promesa más universal: entender el amor, el cuerpo, el humor, la incertidumbre, la exigencia y el malestar contemporáneo desde el psicoanálisis, la literatura y la filosofía. Su propia bio habla de “entender lo que no se deja etiquetar”, y en entrevistas recientes ha trabajado la relación entre humor, ambigüedad, deshumanización y literalidad.

**Riesgo principal para Comfama:** menor que Tamara en clave ideológica directa, pero con un posible problema de sofisticación conceptual. Puede ser muy potente para liderazgo, salud mental, cultura y conversaciones sobre cuidado, pero también puede ser malinterpretada si se edita mal una frase, si se saca de contexto o si se promociona desde titulares demasiado abstractos.

**Brechas que podría exacerbar si se gestiona mal:**
- **Empatía:** si el discurso se vuelve demasiado abstracto o introspectivo.
- **Utilidad:** si el público no ve qué relación tiene con bienestar, vínculos, salud mental o vida cotidiana.
- **Adaptación:** riesgo menor, aunque existe si se comunica desde jerga o excesiva sofisticación.
"""
        },
        "@julian.fuks": {
            "level": "Amarillo",
            "color": "#D4B000",
            "content": """
**Julián Fuks**

Fuks proyecta una autoridad cultural seria, sobria y de alta legitimidad literaria. Su universo gira alrededor de memoria, exilio, dictadura, identidad y autoficción. Eso lo vuelve intelectualmente consistente y reputacionalmente digno, pero no necesariamente masivo ni fácil de traducir a utilidad o cercanía para audiencias amplias.

**Riesgo principal para Comfama:** puede reforzar una percepción de contenido cultural “alto”, serio y valioso, pero también más distante de las brechas de empatía y utilidad si no se aterriza bien. Su riesgo no está en el escándalo, sino en que el evento se sienta demasiado intelectual o poco conectado con la vida cotidiana del afiliado medio. Eso podría dejar neutra la conversación en presencia y empatía, en vez de mejorarla.

**Brechas que podría exacerbar si se gestiona mal:**
- **Presencia / empatía:** por distancia emocional o exceso de densidad discursiva.
- **Utilidad / favorabilidad:** si el público no entiende por qué Comfama lo invita y qué gana con esa conversación.
- **Liderazgo:** puede sumar positivamente si se enmarca como conversación de pensamiento y cultura.

**Lectura táctica:** conviene más para foros de pensamiento, lectura, memoria, ciudadanía o conversación cultural curada; menos para campañas masivas de cercanía o utilidad.
"""
        }
    }
    return analyses.get(profile)

def render_traffic_light(level, color):
    green_active = "#2A8F5B" if level == "Verde" else "rgba(255,255,255,0.15)"
    yellow_active = "#D4B000" if level == "Amarillo" else "rgba(255,255,255,0.15)"
    orange_active = "#D96C1A" if level == "Amarillo rojizo" else "rgba(255,255,255,0.15)"
    red_active = "#D64545" if level == "Rojo" else "rgba(255,255,255,0.15)"

    st.markdown(
        f"""
        <div style="
            display:flex;
            justify-content:center;
            margin-bottom: 18px;
            margin-top: 6px;
        ">
            <div style="
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.10);
                border-radius: 22px;
                padding: 18px 22px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.20);
                min-width: 220px;
            ">
                <div style="text-align:center; color:white; font-size:14px; font-weight:700; letter-spacing:1px; margin-bottom:14px;">
                    SEMÁFORO
                </div>
                <div style="display:flex; justify-content:center; gap:14px;">
                    <div style="width:24px; height:24px; border-radius:50%; background:{green_active}; box-shadow:0 0 14px {green_active};"></div>
                    <div style="width:24px; height:24px; border-radius:50%; background:{yellow_active}; box-shadow:0 0 14px {yellow_active};"></div>
                    <div style="width:24px; height:24px; border-radius:50%; background:{orange_active}; box-shadow:0 0 14px {orange_active};"></div>
                    <div style="width:24px; height:24px; border-radius:50%; background:{red_active}; box-shadow:0 0 14px {red_active};"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_result_card(profile_data):
    render_traffic_light(profile_data["level"], profile_data["color"])

    st.markdown(
        """
        <div style="
            background: linear-gradient(180deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.04) 100%);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 22px;
            padding: 28px;
            margin-top: 8px;
            margin-bottom: 28px;
            box-shadow: 0 14px 35px rgba(0,0,0,0.22);
            backdrop-filter: blur(8px);
        ">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(profile_data["content"])

def render_ranking():
    st.markdown(
        """
## Ranking de conveniencia reputacional para Comfama
"""
    )

    st.markdown(
        """
<div style="
    background: linear-gradient(180deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.04) 100%);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 14px 35px rgba(0,0,0,0.18);
">
    <div style="margin-bottom: 18px;">
        <div style="font-size: 18px; font-weight: 800; color: white;">1. Alexandra Kohan</div>
        <div style="color: rgba(255,255,255,0.88); margin-top: 6px;">
            La pondría primero porque ofrece valor cultural e intelectual, pero con temas más fácilmente traducibles a bienestar, salud mental, vínculos y cuidado, que son marcos más compatibles con Comfama.
        </div>
    </div>
    <div style="margin-bottom: 18px;">
        <div style="font-size: 18px; font-weight: 800; color: white;">2. Julián Fuks</div>
        <div style="color: rgba(255,255,255,0.88); margin-top: 6px;">
            Muy sólido y respetable, pero más útil para agenda cultural o de pensamiento que para corregir brechas de empatía y utilidad en gran escala.
        </div>
    </div>
    <div>
        <div style="font-size: 18px; font-weight: 800; color: white;">3. Tamara Tenenbaum</div>
        <div style="color: rgba(255,255,255,0.88); margin-top: 6px;">
            Muy valiosa editorialmente, pero la de mayor probabilidad de activar lectura ideológica o polarización externa en el contexto reputacional actual de Comfama.
        </div>
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

def render_avatar_section():
    st.markdown(
        "<h2 style='text-align:center; margin-bottom: 18px;'>Asistente de riesgo reputacional</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        """
<div style="
    margin-top: 10px;
    border-radius: 22px;
    overflow: hidden;
    background: linear-gradient(180deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.04) 100%);
    border: 1px solid rgba(255,255,255,0.12);
    padding: 14px;
    box-shadow: 0 14px 35px rgba(0,0,0,0.18);
">
    <iframe
        src="https://embed.liveavatar.com/v1/61048f13-9b1a-4027-baf4-d229ce294a7c"
        allow="microphone"
        title="LiveAvatar Embed"
        style="aspect-ratio: 16/9; width: 100%; border: 0; border-radius: 14px;">
    </iframe>
</div>
""",
        unsafe_allow_html=True
    )

# =========================
# ESTILOS VISUALES
# =========================
background_css = ""
try:
    image_path = "fondo-julius-epm.png"
    bg_b64 = image_to_base64(image_path)
    background_css = f"""
    .stApp {{
        background-image: url("data:image/png;base64,{bg_b64}");
        background-repeat: no-repeat;
        background-position: top center;
        background-size: auto;
        background-attachment: scroll;
    }}
    """
except Exception:
    background_css = """
    .stApp {
        background: linear-gradient(180deg, #150120 0%, #22042E 35%, #240531 100%);
    }
    """

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stApp {{
        font-family: 'Montserrat', sans-serif !important;
    }}

    {background_css}

    .stApp .main .block-container {{
        background-image: linear-gradient(to bottom, transparent 270px, #240531 270px) !important;
        background-repeat: no-repeat !important;
        background-size: 100% 100% !important;
        border-radius: 28px !important;
        padding: 42px 42px 54px 42px !important;
        max-width: 920px !important;
        margin: 1.6rem auto !important;
    }}

    h1, h2, h3, p, li, div, span, label {{
        color: white !important;
    }}

    .stSelectbox label {{
        color: white !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        margin-bottom: 6px !important;
    }}

    div[data-baseweb="select"] > div {{
        background: rgba(255,255,255,0.08) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 16px !important;
        min-height: 52px !important;
        color: white !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }}

    div.stButton {{
        display: flex !important;
        justify-content: center !important;
        margin-top: 8px !important;
    }}

    div.stButton > button {{
        background: linear-gradient(135deg, #FF8A00 0%, #FF6A00 100%) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        letter-spacing: 0.2px !important;
        padding: 12px 34px !important;
        border-radius: 999px !important;
        border: none !important;
        width: auto !important;
        min-width: 180px !important;
        box-shadow: 0 12px 26px rgba(255,122,0,0.28) !important;
        transition: all 0.2s ease-in-out !important;
    }}

    div.stButton > button:hover {{
        background: linear-gradient(135deg, #FF9A1A 0%, #FF7300 100%) !important;
        color: #ffffff !important;
        transform: translateY(-1px);
    }}

    .premium-box {{
        background: linear-gradient(180deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.04) 100%);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 22px;
        padding: 26px;
        margin-bottom: 26px;
        box-shadow: 0 14px 35px rgba(0,0,0,0.18);
        backdrop-filter: blur(8px);
    }}

    .section-divider {{
        height: 1px;
        background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.18) 50%, rgba(255,255,255,0) 100%);
        margin-top: 26px;
        margin-bottom: 26px;
    }}

    .mini-caption {{
        text-align: center;
        color: rgba(255,255,255,0.72);
        font-size: 13px;
        margin-top: -2px;
        margin-bottom: 20px;
        letter-spacing: 0.3px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# ESTADO
# =========================
if "analizado" not in st.session_state:
    st.session_state.analizado = False

if "perfil_seleccionado" not in st.session_state:
    st.session_state.perfil_seleccionado = None

# =========================
# HEADER
# =========================
render_top_logo()
render_comfama_logo()

st.markdown(
    "<h1 style='text-align:center; margin-bottom: 10px;'>Simulador de riesgo reputacional</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="premium-box">
        <h3 style="margin-top:0; text-align:center;">Objetivo</h3>
        <p style="margin-bottom: 10px; text-align:center;">
            Analizar la conveniencia de los perfiles sociales para la estrategia reputacional de Comfama,
            con base en los siguientes criterios:
        </p>
        <div style="display:flex; justify-content:center;">
            <ul style="margin-top: 6px; line-height: 1.9;">
                <li>Tono</li>
                <li>Estilo</li>
                <li>Discurso</li>
                <li>Audiencia</li>
                <li>Contenido</li>
                <li>Temáticas abordadas</li>
                <li>Posturas</li>
            </ul>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# FORMULARIO PRINCIPAL
# =========================
perfil = st.selectbox(
    "Selecciona el perfil a analizar:",
    ["@tamtenenbaum", "@alexkohan", "@julian.fuks"]
)

st.markdown("<div class='mini-caption'>Selecciona un perfil y ejecuta el análisis reputacional.</div>", unsafe_allow_html=True)

if st.button("Analizar"):
    with st.spinner("Analizando tono, discurso, audiencias y riesgos reputacionales..."):
        time.sleep(2.8)
    st.session_state.analizado = True
    st.session_state.perfil_seleccionado = perfil

# =========================
# RESULTADO
# =========================
if st.session_state.analizado and st.session_state.perfil_seleccionado:
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Resultado del análisis</h2>", unsafe_allow_html=True)
    profile_data = get_profile_analysis(st.session_state.perfil_seleccionado)
    render_result_card(profile_data)
    render_ranking()
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    render_avatar_section()
else:
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    render_avatar_section()
