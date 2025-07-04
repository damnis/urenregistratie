# projecten.py
def get_projecten():
    try:
        with open("projecten.txt", "r") as f:
            projecten = [lijn.strip() for lijn in f.readlines()]
    except FileNotFoundError:
        projecten = []
    return projecten

def voeg_project_toe(naam):
    projecten = get_projecten()
    if naam not in projecten:
        with open("projecten.txt", "a") as f:
            f.write(f"{naam}\n")
