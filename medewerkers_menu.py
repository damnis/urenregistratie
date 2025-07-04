import streamlit as st
from medewerkers import get_medewerkers, voeg_medewerker_toe, get_medewerkers_dict

def medewerkers_menu():
    st.header("Instellingen")

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


















# wit
