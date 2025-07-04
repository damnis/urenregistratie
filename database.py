import sqlite3

def init_db():
    conn = sqlite3.connect("facturatie.db")
    c = conn.cursor()

    c.execute('''
       CREATE TABLE IF NOT EXISTS uren (
            id INTEGER PRIMARY KEY,
            medewerker TEXT,
            klant TEXT,
            project TEXT,
            datum TEXT,
            starttijd TEXT,
            eindtijd TEXT,
            uren REAL,
            omschrijving TEXT
            factuurstatus TEXT
        ) 
        
    ''')

    conn.commit()
    conn.close()
