import streamlit as st
from projecten import get_projecten, voeg_project_toe

def project_menu():
    # Project toevoegen
    st.subheader("werkcode toevoegen")
    nieuw_project = st.text_input("Nieuwe werkcode")
    if st.button("Toevoegen werkcode"):
        if nieuw_project:
            voeg_project_toe(nieuw_project)
            st.success(f"Project '{nieuw_project}' toegevoegd.")
        else:
            st.warning("Voer een werkcode in.")
    st.write("📋 Bestaande projecten:")
    st.write(get_projecten())

    




















# wit
