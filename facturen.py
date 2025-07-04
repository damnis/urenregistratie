import streamlit as st
import pandas as pd
import sqlite3
from pdf_generator import maak_pdf

def genereer_factuur():
    st.header("Factuur genereren")

    conn = sqlite3.connect("facturatie.db")
    df = pd.read_sql_query("SELECT * FROM uren", conn)
    conn.close()

    klant = st.selectbox("Klant", sorted(df["klant"].unique()))
    klant_data = df[df["klant"] == klant]

    st.dataframe(klant_data)

    if st.button("Maak PDF"):
        maak_pdf(klant, klant_data)
        st.success("PDF gegenereerd!")
