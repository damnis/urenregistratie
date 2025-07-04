import streamlit as st
import sqlite3
from datetime import date

def invoer_uren():
    st.header("Uren Invoeren")

    klant = st.text_input("Klantnaam")
    project = st.text_input("Project")
    datum = st.date_input("Datum", date.today())
    uren = st.number_input("Aantal uur", min_value=0.25, step=0.25)
    omschrijving = st.text_area("Omschrijving")

    if st.button("Opslaan"):
        conn = sqlite3.connect("facturatie.db")
        c = conn.cursor()
        c.execute("INSERT INTO uren (klant, project, datum, uren, omschrijving) VALUES (?, ?, ?, ?, ?)",
                  (klant, project, datum.isoformat(), uren, omschrijving))
        conn.commit()
        conn.close()
        st.success("Uren opgeslagen!")
