import streamlit as st
from klanten import get_klanten, voeg_klant_toe

def instellingen_menu():
    st.header("Instellingen")

    st.subheader("Klant toevoegen")
    nieuwe_klant = st.text_input("Naam nieuwe klant")

    if st.button("Toevoegen"):
        if nieuwe_klant:
            voeg_klant_toe(nieuwe_klant)
            st.success(f"Klant '{nieuwe_klant}' toegevoegd.")
        else:
            st.warning("Voer een naam in.")

    st.subheader("Bestaande klanten")
    st.write(get_klanten())


# ------

from projecten import get_projecten, voeg_project_toe

st.subheader("Project toevoegen")
nieuw_project = st.text_input("Nieuw project (bijv. 110 - financiële administratie)")

if st.button("Toevoegen project"):
    if nieuw_project:
        voeg_project_toe(nieuw_project)
        st.success(f"Project '{nieuw_project}' toegevoegd.")
    else:
        st.warning("Voer een projectnaam in.")

st.subheader("Bestaande projecten")
st.write(get_projecten())


# -------
from medewerkers import get_medewerkers, voeg_medewerker_toe

st.subheader("Medewerker toevoegen")
nieuwe_medewerker = st.text_input("Naam nieuwe medewerker")

if st.button("Toevoegen medewerker"):
    if nieuwe_medewerker:
        voeg_medewerker_toe(nieuwe_medewerker)
        st.success(f"Medewerker '{nieuwe_medewerker}' toegevoegd.")
    else:
        st.warning("Voer een naam in.")

st.subheader("Bestaande medewerkers")
st.write(get_medewerkers())














# -------
