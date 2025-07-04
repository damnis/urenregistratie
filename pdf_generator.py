from fpdf import FPDF

def maak_pdf(klant, df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Factuur voor: {klant}", ln=True)

    for index, row in df.iterrows():
        regel = f"{row['datum']} - {row['project']} - {row['uren']}u: {row['omschrijving']}"
        pdf.cell(200, 10, txt=regel, ln=True)

    pdf.output(f"factuur_{klant}.pdf")
