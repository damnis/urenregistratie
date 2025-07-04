import streamlit as st
import sqlite3
from datetime import datetime, date, time, timedelta
from klanten import get_klanten
from projecten import get_projecten
from medewerkers import get_medewerkers  # nog te maken!

def invoer_uren():
    st.header("Uren Invoeren")

    # Medewerkerselectie
    medewerker = st.selectbox("Medewerker", options=get_medewerkers())

    # Datumselectie
    datum = st.date_input("Datum", value=date.today())

    # Klantselectie (met mogelijkheid om te typen)
    klant = st.selectbox("Klant", options=get_klanten())

    # Projectselectie
    project = st.selectbox("Project", options=get_projecten())

    # Begintijd en eindtijd (in kolommen)
    col1, col2 = st.columns(2)
    with col1:
        starttijd = st.time_input("Begintijd", value=time(9, 0), step=timedelta(minutes=15))
    with col2:
        eindtijd = st.time_input("Eindtijd", value=time(17, 0), step=timedelta(minutes=15))

    # Berekening van uren
    start_dt = datetime.combine(datum, starttijd)
    eind_dt = datetime.combine(datum, eindtijd)

    if eind_dt > start_dt:
        berekende_uren = round((eind_dt - start_dt).total_seconds() / 3600, 2)
        st.success(f"Berekend aantal uren: {berekende_uren}")
    else:
        berekende_uren = 0
        st.warning("Eindtijd moet na begintijd liggen!")

    # Aantal uren (corrigeerbaar indien nodig)
    uren = st.number_input("Aantal uur (aanpassen indien nodig)", value=berekende_uren, min_value=0.0, step=0.25)

    # Omschrijving werk
    omschrijving = st.text_area("Omschrijving")

    # Opslaan in database
    if st.button("Opslaan"):
        conn = sqlite3.connect("facturatie.db")
        c = conn.cursor()
        c.execute("""
            INSERT INTO uren (medewerker, klant, project, datum, starttijd, eindtijd, uren, omschrijving)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            medewerker,
            klant,
            project,
            datum.isoformat(),
            starttijd.strftime('%H:%M'),
            eindtijd.strftime('%H:%M'),
            uren,
            omschrijving
        ))
        conn.commit()
        conn.close()
        st.success("Uren succesvol opgeslagen!")
