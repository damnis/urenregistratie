def get_project_dict():
    return {
        "110": "Financiële administratie",
        "210": "Aanleggen dossier",
        "810": "Advies",
        "820": "Management",
        # enz.
    }

def get_projecten():
    # Voor dropdown: "110 - Financiële administratie"
    d = get_project_dict()
    return [f"{code} - {naam}" for code, naam in d.items()]
