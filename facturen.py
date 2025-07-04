import streamlit as st
import pandas as pd
import sqlite3
from datetime import date
from factuurstatus import get_factuurstatussen, default_status
from klanten import get_klanten
from projecten import get_projecten
from medewerkers import get_medewerkers

def genereer_factuur():
    st.header("📄 Facturen genereren")

    # Ophalen data
    conn = sqlite3.connect("facturatie.db")
    df = pd.read_sql_query("SELECT * FROM uren", conn)

    # Alleen 'te factureren'
    df = df[df["factuurstatus"] == default_status()]
    df["datum"] = pd.to_datetime(df["datum"])

    if df.empty:
        st.info("Geen uren beschikbaar met status 'te factureren'.")
        return

    # Filters
    min_datum = df["datum"].min().date()
    max_datum = df["datum"].max().date()

    st.subheader("📅 Periode")
    col1, col2 = st.columns(2)
    with col1:
        start_datum = st.date_input("Vanaf", value=min_datum)
    with col2:
        eind_datum = st.date_input("Tot en met", value=max_datum)

    st.subheader("📌 Filters")
    klanten = st.multiselect("Klant(en)", options=sorted(df["klant"].unique().tolist()), default=df["klant"].unique())
    medewerkers = st.multiselect("Medewerker(s)", options=sorted(df["medewerker"].unique().tolist()), default=df["medewerker"].unique())
    projecten = st.multiselect("Project(en)", options=sorted(df["project"].unique().tolist()), default=df["project"].unique())

    df_filtered = df[
        (df["datum"] >= pd.to_datetime(start_datum)) &
        (df["datum"] <= pd.to_datetime(eind_datum)) &
        (df["klant"].isin(klanten)) &
        (df["medewerker"].isin(medewerkers)) &
        (df["project"].isin(projecten))
    ]

    if df_filtered.empty:
        st.warning("Geen uren gevonden in de selectie.")
        return

    # Toon overzicht
    st.subheader("💬 Uren die gefactureerd worden")
    st.dataframe(df_filtered)

    if st.button("✅ Bevestig en genereer factuur/facturen"):
        from fpdf import FPDF

        for klant in df_filtered["klant"].unique():
            df_klant = df_filtered[df_filtered["klant"] == klant]

            # PDF maken per klant
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Factuur voor {klant}", ln=True)

            totaal = 0
            for i, row in df_klant.iterrows():
                regel = f"{row['datum'].date()} - {row['project']} - {row['medewerker']} - {row['uren']}u"
                pdf.cell(200, 8, txt=regel, ln=True)
                totaal += float(row["uren"])  # Tarief nog toevoegen

            pdf.cell(200, 10, txt=f"Totaal aantal uren: {totaal}", ln=True)
            filename = f"factuur_{klant.replace(' ', '_')}.pdf"
            pdf.output(filename)

            # Zet status op 'gefactureerd'
            ids = df_klant["id"].tolist()
            c = conn.cursor()
            c.executemany("UPDATE uren SET factuurstatus = 'gefactureerd' WHERE id = ?", [(i,) for i in ids])
            conn.commit()

        st.success("Facturen gegenereerd en status bijgewerkt.")

    conn.close()
