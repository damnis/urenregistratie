import streamlit as st 
from klanten import get_klanten, voeg_klant_toe 
from projecten import get_projecten, get_project_dict  # voeg_project_toe 
from locatie import get_locatie, voeg_locatie_toe 
from medewerkers import get_medewerkers, voeg_medewerker_toe, get_medewerkers_dict 
from prijsafspraak import get_prijsafspraken


def instellingen_menu(): st.header("Instellingen")

# Klant toevoegen
st.subheader("Klant toevoegen")
nieuwe_klant = st.text_input("Naam nieuwe klant")
vaste_prijs = st.number_input("Vaste prijsafspraak (optioneel)", min_value=0.0, value=0.0, step=50.0, format="%.2f")
uitzonderingscodes = st.text_input("Projectcodes uitsluiten (komma-gescheiden, bijv. 810,820)")

if st.button("Toevoegen klant"):
    if nieuwe_klant:
        voeg_klant_toe(nieuwe_klant)
        if vaste_prijs > 0:
            # Opslaan prijsafspraak als regel in prijsafspraken.txt (optioneel)
            with open("prijsafspraken.txt", "a") as f:
                f.write(f"{nieuwe_klant}|{vaste_prijs}|{uitzonderingscodes}\n")
        st.success(f"Klant '{nieuwe_klant}' toegevoegd.")
    else:
        st.warning("Voer een naam in.")

st.write("📋 Bestaande klanten:")
st.write(get_klanten())


#def instellingen_menu():
 #   st.header("Instellingen")

    # Klant toevoegen
#    st.subheader("Klant toevoegen")
#    nieuwe_klant = st.text_input("Naam nieuwe klant")
#    if st.button("Toevoegen klant"):
#        if nieuwe_klant:
#            voeg_klant_toe(nieuwe_klant)
 #           st.success(f"Klant '{nieuwe_klant}' toegevoegd.")
 #       else:
#            st.warning("Voer een naam in.")
#    st.write("📋 Bestaande klanten:")
 #   st.write(get_klanten())

def project_menu():
    # Project toevoegen - verplaatst
    st.subheader("Project toevoegen")
    nieuw_project = st.text_input("Nieuw project")
    if st.button("Toevoegen project"):
        if nieuw_project:
            voeg_project_toe(nieuw_project)
            st.success(f"Project '{nieuw_project}' toegevoegd.")
        else:
            st.warning("Voer een projectnaam in.")
    st.write("📋 Bestaande projecten:")
    st.write(get_projecten())

def medewerkers_menu():
    # Medewerker toevoegen - verplaatst
    st.subheader("Medewerker toevoegen")
    nieuwe_medewerker = st.text_input("Naam nieuwe medewerker")
    nieuw_tarief = st.number_input("Tarief per uur (EUR)", min_value=0.0, step=5.0)
    if st.button("Toevoegen locatie"):
        if nieuwe_locatie:
            voeg_locatie_toe(nieuwe_locatie)
            st.success(f"Locatie '{nieuwe_locatie}' toegevoegd.")
        else:
            st.warning("Voer een naam in.")
    st.write("📋 Bestaande medewerkers + tarieven:")
    st.write(get_medewerkers_dict())

def locatie_menu():
    # Locatie toevoegen - verplaatst
    st.subheader("Locatie toevoegen")
    nieuwe_locatie = st.text_input("Naam nieuwe locatie")
    if st.button("Toevoegen locatie"):
        if nieuwe_locatie:
            voeg_locatie_toe(nieuwe_locatie)
            st.success(f"Locatie '{nieuwe_locatie}' toegevoegd.")
        else:
            st.warning("Voer een locatie in.")
    st.write("📋 Bestaande locaties")
    st.write(get_locatie())






















# wit
