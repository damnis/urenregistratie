import streamlit as st
from klanten import get_klanten, voeg_klant_toe
from projecten import get_projecten, voeg_project_toe
from medewerkers import get_medewerkers, voeg_medewerker_toe, get_medewerkers_dict

def instellingen_menu():
    st.header("Instellingen")

    # Klant toevoegen
    st.subheader("Klant toevoegen")
    nieuwe_klant = st.text_input("Naam nieuwe klant")
    if st.button("Toevoegen klant"):
        if nieuwe_klant:
            voeg_klant_toe(nieuwe_klant)
            st.success(f"Klant '{nieuwe_klant}' toegevoegd.")
        else:
            st.warning("Voer een naam in.")
    st.write("📋 Bestaande klanten:")
    st.write(get_klanten())

    # Project toevoegen
    st.subheader("Project toevoegen")
    nieuw_project = st.text_input("Nieuw project")
    if st.button("Toevoegen project"):
        if nieuw_project:
            voeg_project_toe(nieuw_project)
            st.success(f"Project '{nieuw_project}' toegevoegd.")
        else:
            st.warning("Voer een projectnaam in.")
    st.write("📋 Bestaande projecten:")
    st.write(get_projecten())

    # Medewerker toevoegen
    st.subheader("Medewerker toevoegen")
    nieuwe_medewerker = st.text_input("Naam nieuwe medewerker")
    nieuw_tarief = st.number_input("Tarief per uur (EUR)", min_value=0.0, step=5.0)
    if st.button("Toevoegen medewerker"):
        if nieuwe_medewerker:
            voeg_medewerker_toe(nieuwe_medewerker, nieuw_tarief)
            st.success(f"Medewerker '{nieuwe_medewerker}' toegevoegd met tarief €{nieuw_tarief}/uur.")
        else:
            st.warning("Voer een naam in.")
    st.write("📋 Bestaande medewerkers + tarieven:")
    st.write(get_medewerkers_dict())
