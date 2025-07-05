def get_prijsafspraken():
    return {
        "klant1": {
            "prijs": 500.00,
            "uitsluiten": ["810", "820"]  # of beginnend met '8'
        },
        "klant2": {
            "prijs": 750.00,
            "uitsluiten": ["820"]
        }
    }

def get_vaste_prijs(klant):
    afspraken = get_prijsafspraken()
    return afspraken.get(klant, None)
