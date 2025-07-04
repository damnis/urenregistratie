# klanten.py
def get_klanten():
    try:
        with open("klanten.txt", "r") as f:
            klanten = [lijn.strip() for lijn in f.readlines()]
    except FileNotFoundError:
        klanten = []
    return klanten

def voeg_klant_toe(naam):
    klanten = get_klanten()
    if naam not in klanten:
        with open("klanten.txt", "a") as f:
            f.write(f"{naam}\n")
