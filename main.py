import streamlit as st
from uren import invoer_uren
from overzicht import toon_overzicht
from facturen import genereer_factuur
from instellingen import instellingen_menu
from projectmenu import project_menu
from database import init_db
init_db()

# Zet pagina-instellingen
st.set_page_config(page_title="Urenregistratie & Facturatie", layout="wide")

# Toon logo bovenaan
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://www.kage.nl/newcms/wp/wp-content/uploads/cropped-Kage-ConsultLogo300.png' width='300'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Titel van de app (optioneel)
st.title("🧾 Urenregistratie en Facturatie App")

# Sidebar-menu
pagina = st.sidebar.selectbox("📂 Kies een pagina", [
    "Uren invoer",
    "Overzicht",
    "Factuur maken",
    "Instellingen"
])

# Paginaweergave
if pagina == "Uren invoer":
    invoer_uren()
elif pagina == "Overzicht":
    toon_overzicht()
elif pagina == "Factuur maken":
    genereer_factuur()
elif pagina == "Instellingen":
    instellingen_menu()
