import streamlit as st
import sqlite3
from datetime import date
from klanten import get_klanten
from projecten import get_projecten
from datetime import datetime, date, time, timedelta

def invoer_uren():
    st.header("Uren Invoeren")
# medewerker selectie - moet mog gedefineerd worden   !!!
medewerker = st.selectbox("Medewerker", options=get_medewerkers())
# datumvan vandaag (ingevuld kan wijzigen)
datum = st.date_input("Datum", value=date.today())
# voer klant in (ik moet ook in de selectbox kunnen typen en de juiste naam krijgen, deze lijst is lang)
klant = st.selectbox("Klant", options=get_klanten())
# voer project in (geen bijzonderheden)
project = st.selectbox("Project", options=get_projecten())

col1, col2 = st.columns(2)
with col1:
    starttijd = st.time_input("Begintijd", value=time(9, 0), step=timedelta(minutes=15))
with col2:
    eindtijd = st.time_input("Eindtijd", value=time(17, 0), step=timedelta(minutes=15))

# Bereken verschil in uren
start_dt = datetime.combine(datum, starttijd)
eind_dt = datetime.combine(datum, eindtijd)

if eind_dt > start_dt:
    berekende_uren = round((eind_dt - start_dt).total_seconds() / 3600, 2)
    st.success(f"Berekend aantal uren: {berekende_uren}")
else:
    berekende_uren = 0
    st.warning("Eindtijd moet na begintijd liggen!")

# Correctiemogelijkheid (korting, afronding, afronding naar halve uren enz.)
uren = st.number_input("Aantal uur (aanpassen indien nodig)", value=berekende_uren, min_value=0.0, step=0.25)

    
 #   aanvullend: min of plus uren toevoegen aan de berekende uren (extra regel, geen correctie)
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
