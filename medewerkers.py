# medewerkers.py

def get_medewerkers():
    try:
        with open("medewerkers.txt", "r") as f:
            return [lijn.strip() for lijn in f.readlines()]
    except FileNotFoundError:
        return []

def voeg_medewerker_toe(naam):
    medewerkers = get_medewerkers()
    if naam not in medewerkers:
        with open("medewerkers.txt", "a") as f:
            f.write(f"{naam}\n")
