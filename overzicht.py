import streamlit as st
import pandas as pd
import sqlite3

def toon_overzicht():
    st.header("Overzicht Uren")

    conn = sqlite3.connect("facturatie.db")
    df = pd.read_sql_query("SELECT * FROM uren", conn)
    conn.close()

    klant_filter = st.selectbox("Filter op klant", options=["Alle"] + sorted(df["klant"].unique().tolist()))
    if klant_filter != "Alle":
        df = df[df["klant"] == klant_filter]

    st.dataframe(df)

    if st.button("Download als CSV"):
        st.download_button("⬇️ Download CSV", df.to_csv(index=False), "uren.csv", "text/csv")
