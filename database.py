import sqlite3

def init_db():
    conn = sqlite3.connect("facturatie.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS uren (
            id INTEGER PRIMARY KEY,
            klant TEXT,
            project TEXT,
            datum TEXT,
            uren REAL,
            omschrijving TEXT
        )
    ''')

    conn.commit()
    conn.close()
