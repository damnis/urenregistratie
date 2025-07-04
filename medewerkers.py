# medewerkers.py

def get_medewerkers_dict():
    try:
        with open("medewerkers.txt", "r") as f:
            regels = [lijn.strip() for lijn in f.readlines()]
    except FileNotFoundError:
        regels = []

    medewerkers = {}
    for regel in regels:
        parts = regel.split("|")
        naam = parts[0].strip()
        tarief = float(parts[1]) if len(parts) > 1 else 0.0
        medewerkers[naam] = tarief
    return medewerkers

def get_medewerkers():
    return list(get_medewerkers_dict().keys())

def get_tarief(medewerker):
    return get_medewerkers_dict().get(medewerker, 0.0)

def voeg_medewerker_toe(naam, tarief):
    medewerkers = get_medewerkers()
    if naam not in medewerkers:
        with open("medewerkers.txt", "a") as f:
            f.write(f"{naam} | {tarief}\n")# medewerkers.py

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
