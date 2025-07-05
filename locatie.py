# locatie.py
def get_locatie():
    try:
        with open("locatie.txt", "r") as f:
            locatie = [lijn.strip() for lijn in f.readlines()]
    except FileNotFoundError:
        locatie = []
    return locatie 

def voeg_locatie_toe(naam):
    locatie = get_locatie()
    if naam not in locatie:
        with open("locatie.txt", "a") as f:
            f.write(f"{naam}\n")
