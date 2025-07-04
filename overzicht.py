import streamlit as st
import pandas as pd
import sqlite3
from datetime import date

def toon_overzicht():
    st.header("Overzicht Uren")

    with st.expander("📊 Toon uitgebreid overzicht"):

        # Connectie en data ophalen
        conn = sqlite3.connect("facturatie.db")
        df = pd.read_sql_query("SELECT * FROM uren", conn)
        conn.close()

        if df.empty:
            st.warning("Nog geen gegevens beschikbaar.")
            return

        # Datumfilter bovenaan
        df["datum"] = pd.to_datetime(df["datum"])
        min_datum = df["datum"].min().date()
        max_datum = df["datum"].max().date()

        col1, col2 = st.columns(2)
        with col1:
            start_datum = st.date_input("Vanaf datum", min_value=min_datum, max_value=max_datum, value=min_datum)
        with col2:
            eind_datum = st.date_input("Tot en met", min_value=min_datum, max_value=max_datum, value=max_datum)

        df = df[(df["datum"] >= pd.to_datetime(start_datum)) & (df["datum"] <= pd.to_datetime(eind_datum))]

        # Filters op basis van gefilterde datumreeks
        medewerkers = st.multiselect("Selecteer medewerker(s)", options=sorted(df["medewerker"].unique().tolist()), default=df["medewerker"].unique())
        klanten = st.multiselect("Selecteer klant(en)", options=sorted(df["klant"].unique().tolist()), default=df["klant"].unique())
        projecten = st.multiselect("Selecteer project(en)", options=sorted(df["project"].unique().tolist()), default=df["project"].unique())

        # Filter de dataframe
        df_filtered = df[
            df["medewerker"].isin(medewerkers) &
            df["klant"].isin(klanten) &
            df["project"].isin(projecten)
        ]

        st.dataframe(df_filtered)

        # Totalen per type
        st.subheader("📈 Samenvattingen")
        totalen_type = st.selectbox("Toon totalen per:", ["Medewerker", "Klant", "Project"])
        kolom = totalen_type.lower()
        st.dataframe(df_filtered.groupby(kolom)["uren"].sum().reset_index().rename(columns={"uren": "Totaal uren"}))

        totaal = df_filtered["uren"].sum()
        st.success(f"🕒 Totale uren in selectie: {totaal}")

        # Exporteer als CSV
        st.download_button("⬇️ Download als CSV", data=df_filtered.to_csv(index=False), file_name="urenoverzicht.csv", mime="text/csv")

        # PDF-export (eenvoudig)
        if st.button("📄 Download als PDF"):
            from fpdf import FPDF

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Urenoverzicht", ln=True)

            for index, row in df_filtered.iterrows():
                regel = f"{row['datum'].date()} - {row['medewerker']} - {row['project']} - {row['klant']} - {row['uren']}u"
                pdf.cell(200, 8, txt=regel, ln=True)

            pdf.output("urenoverzicht.pdf")
            st.success("PDF gegenereerd (lokaal opgeslagen als 'urenoverzicht.pdf')")
