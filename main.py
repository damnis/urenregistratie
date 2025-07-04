import streamlit as st
from uren import invoer_uren
from overzicht import toon_overzicht
from facturen import genereer_factuur
from instellingen import instellingen_menu
from database import init_db
init_db()

st.set_page_config(page_title="Uren & Facturatie", layout="wide")

menu = st.sidebar.selectbox("Menu", ["Uren invoer", "Overzicht", "Factuur maken", "Instellingen"])

if menu == "Uren invoer":
    invoer_uren()
elif menu == "Overzicht":
    toon_overzicht()
elif menu == "Factuur maken":
    genereer_factuur()
elif menu == "Instellingen":
    instellingen_menu()
