import streamlit as st
from PIL import Image
import base64
import io

# =========================
# CONFIGURACIÓN DE PÁGINA
# =========================
st.set_page_config(
    page_title="Asistente de riesgo reputacional - Comfama",
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
    """
    Logo principal de Julius, usando el recurso local del diseño original.
    """
    logo_path = "logo-julius.png"
    try:
        img_b64 = image_to_base64(logo_path)
        st.markdown(
            f"""
            <div style='display:flex; justify-content:center; margin-top: 10px; margin-bottom: 8px;'>
                <img src="data:image/png;base64,{img_b64}" width="150px"/>
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
    """
    Logo externo solicitado por el usuario, debajo del logo actual de Julius.
    """
    comfama_logo_url = (
        "https://www.comfama.com/servicio-de-empleo/_gatsby/image/"
        "c5db45b591a70aadee27dc99cc568772/ac9159c9c186998eda3ce1ef38d6e292/"
        "logo_comfama.webp?u=https%3A%2F%2Fimages.ctfassets.net%2F203frbsx1z3n%2F"
        "2QY4vQqWGmpccWpnlVDJs2%2F6ec2ad2d8abede6605c917820904118d%2Flogo_comfama.png"
        "&a=w%3D650%26h%3D216%26fm%3Dwebp%26q%3D85&cd=2025-12-17T16%3A25%3A35.387Z"
    )
    st.markdown(
        f"""
        <div style='display:flex; justify-content:center; margin-bottom: 28px;'>
            <img src="{comfama_logo_url}" width="230px"/>
        </div>
        """,
        unsafe_allow_html=True
    )

def get_profile_analysis(profile):
    analyses = {
        "@tamtenenbaum": {
            "label": "Amarillo rojizo",
            "color": "#D96C1A",
            "emoji": "🟠",
            "content": """
**Tamara Tenenbaum — Amarillo rojizo**

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
            "label": "Amarillo",
            "color": "#D4B000",
            "emoji": "🟡",
            "content": """
**Alexandra Kohan — Amarillo**

Kohan ocupa un lugar interesante porque combina densidad intelectual con una promesa más universal: entender el amor, el cuerpo, el humor, la incertidumbre, la exigencia y el malestar contemporáneo desde el psicoanálisis, la literatura y la filosofía. Su propia bio habla de “entender lo que no se deja etiquetar”, y en entrevistas recientes ha trabajado la relación entre humor, ambigüedad, deshumanización y literalidad.

**Riesgo principal para Comfama:** menor que Tamara en clave ideológica directa, pero con un posible problema de sofisticación conceptual. Puede ser muy potente para liderazgo, salud mental, cultura y conversaciones sobre cuidado, pero también puede ser malinterpretada si se edita mal una frase, si se saca de contexto o si se promociona desde titulares demasiado abstractos.

**Brechas que podría exacerbar si se gestiona mal:**
- **Empatía:** si el discurso se vuelve demasiado abstracto o introspectivo.
- **Utilidad:** si el público no ve qué relación tiene con bienestar, vínculos, salud mental o vida cotidiana.
- **Adaptación:** riesgo menor, aunque existe si se comunica desde jerga o excesiva sofisticación.
"""
        },
        "@julian.fuks": {
            "label": "Amarillo",
            "color": "#D4B000",
            "emoji": "🟡",
            "content": """
**Julián Fuks — Amarillo**

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

def render_result_card(profile_data):
    st.markdown(
        f"""
        <div style="
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 18px;
            padding: 22px;
            margin-top: 18px;
            margin-bottom: 24px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.18);
        ">
            <div style="margin-bottom:14px;">
                <span style="
                    display:inline-block;
                    background:{profile_data['color']};
                    color:white;
                    font-weight:700;
                    padding:8px 14px;
                    border-radius:999px;
                    font-size:14px;
                ">
                    {profile_data['emoji']} Semáforo IA: {profile_data['label']}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(profile_data["content"])

def render_ranking():
    st.markdown("## Ranking de conveniencia reputacional para Comfama")
    st.markdown(
        """
**1. Alexandra Kohan**  
La pondría primero porque ofrece valor cultural e intelectual, pero con temas más fácilmente traducibles a bienestar, salud mental, vínculos y cuidado, que son marcos más compatibles con Comfama.

**2. Julián Fuks**  
Muy sólido y respetable, pero más útil para agenda cultural o de pensamiento que para corregir brechas de empatía y utilidad en gran escala.

**3. Tamara Tenenbaum**  
Muy valiosa editorialmente, pero la de mayor probabilidad de activar lectura ideológica o polarización externa en el contexto reputacional actual de Comfama.
"""
    )

def render_avatar_section():
    st.markdown("## Asistente de riesgo reputacional")
    st.markdown(
        """
<div style="margin-top: 12px; border-radius: 18px; overflow: hidden; background: rgba(255,255,255,0.04); padding: 10px;">
    <iframe
        src="https://embed.liveavatar.com/v1/61048f13-9b1a-4027-baf4-d229ce294a7c"
        allow="microphone"
        title="LiveAvatar Embed"
        style="aspect-ratio: 16/9; width: 100%; border: 0; border-radius: 12px;">
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
        background: linear-gradient(180deg, #1b0228 0%, #240531 35%, #240531 100%);
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
        border-radius: 24px !important;
        padding: 40px 40px 50px 40px !important;
        max-width: 900px !important;
        margin: 1.5rem auto !important;
    }}

    h1, h2, h3 {{
        color: white !important;
    }}

    p, li, div, span, label {{
        color: white !important;
    }}

    .stSelectbox label {{
        color: white !important;
        font-weight: 600 !important;
        font-size: 0.98rem !important;
    }}

    div[data-baseweb="select"] > div {{
        background-color: rgba(255,255,255,0.08) !important;
        border: 1px solid rgba(255,255,255,0.18) !important;
        border-radius: 14px !important;
        color: white !important;
    }}

    div.stButton > button {{
        background-color: #FF7A00 !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 12px 24px !important;
        border-radius: 999px !important;
        border: none !important;
        width: 100% !important;
        margin-top: 10px !important;
        transition: all 0.2s ease-in-out !important;
    }}

    div.stButton > button:hover {{
        background-color: #E56E00 !important;
        color: #ffffff !important;
        transform: translateY(-1px);
    }}

    .objective-box {{
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.16);
    }}

    .section-divider {{
        height: 1px;
        background: rgba(255,255,255,0.10);
        margin-top: 24px;
        margin-bottom: 24px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# HEADER
# =========================
render_top_logo()
render_comfama_logo()

st.markdown(
    "<h1 style='text-align:center; margin-bottom: 10px;'>Asistente de riesgo reputacional - Comfama</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="objective-box">
        <h3 style="margin-top:0;">Objetivo</h3>
        <p style="margin-bottom: 10px;">
            Analizar la conveniencia de los perfiles sociales para la estrategia reputacional de Comfama,
            con base en los siguientes criterios:
        </p>
        <ul style="margin-top: 0;">
            <li>Tono</li>
            <li>Estilo</li>
            <li>Discurso</li>
            <li>Audiencia</li>
            <li>Contenido</li>
            <li>Temáticas abordadas</li>
            <li>Posturas</li>
        </ul>
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

if "analizado" not in st.session_state:
    st.session_state.analizado = False

if "perfil_seleccionado" not in st.session_state:
    st.session_state.perfil_seleccionado = None

if st.button("Analizar"):
    st.session_state.analizado = True
    st.session_state.perfil_seleccionado = perfil

# =========================
# RESULTADO
# =========================
if st.session_state.analizado and st.session_state.perfil_seleccionado:
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("## Resultado del análisis")
    profile_data = get_profile_analysis(st.session_state.perfil_seleccionado)
    render_result_card(profile_data)
    render_ranking()
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    render_avatar_section()
else:
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    render_avatar_section()