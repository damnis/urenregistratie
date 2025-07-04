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
