import streamlit as st
import pandas as pd
import sqlite3
from datetime import date
from factuurstatus import get_factuurstatussen, default_status
from klanten import get_klanten
from projecten import get_project_dict
from medewerkers import get_medewerkers
from prijsafspraak import get_vaste_prijs

project_dict = get_project_dict()

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
            prijsafspraak = get_vaste_prijs(klant)

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Factuur voor {klant}", ln=True)

            totaal_uren = 0
            totaal_bedrag = 0
            uitzonderingsregels = []

            if prijsafspraak:
                uitzonderingen = prijsafspraak.get("uitsluiten", [])
                vaste_prijs = prijsafspraak.get("prijs", 0)

                for i, row in df_klant.iterrows():
                    if row["project"].startswith(tuple(uitzonderingen)):
                        omschrijving = project_dict.get(row["project"], row["project"])
                        regel = f"{row['datum'].date()} - {omschrijving} - {row['medewerker']} - {row['uren']}u"
                        pdf.cell(200, 8, txt=regel, ln=True)
                        totaal_uren += float(row["uren"])
                    else:
                        uitzonderingsregels.append(row["id"])

                
                # 💬 Toon het verwachte factuurtotaal in euro
                st.write(f"**Verwacht te factureren bedrag voor {klant}: € {totaal_bedrag:.2f}**")

                pdf.cell(200, 10, txt=f"Vaste prijsafspraak: €{vaste_prijs:.2f}", ln=True)
                totaal_bedrag += vaste_prijs

            else:
                for i, row in df_klant.iterrows():
                    omschrijving = project_dict.get(row["project"], row["project"])
                    regel = f"{row['datum'].date()} - {omschrijving} - {row['medewerker']} - {row['uren']}u"
                    pdf.cell(200, 8, txt=regel, ln=True)
                    totaal_uren += float(row["uren"])

                # 💬 Toon het verwachte factuurtotaal in euro
                st.write(f"**Verwacht te factureren bedrag voor {klant}: € {totaal_bedrag:.2f}**")

            
            pdf.cell(200, 10, txt=f"Totaal aantal uren: {totaal_uren}", ln=True)
            filename = f"factuur_{klant.replace(' ', '_')}.pdf"
            pdf.output(filename)
            with open(filename, "rb") as f:
                st.download_button(
                    label=f"⬇️ Download factuur voor {klant}",
                    data=f,
                    file_name=filename,
                    mime="application/pdf"
                )

            # Update status naar 'gefactureerd'
            ids = df_klant["id"].tolist()
            c = conn.cursor()
            c.executemany("UPDATE uren SET factuurstatus = 'gefactureerd' WHERE id = ?", [(i,) for i in ids])
            conn.commit()

        st.success("Facturen gegenereerd en status bijgewerkt.")

    conn.close()
