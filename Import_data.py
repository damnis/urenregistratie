import sqlite3
import pandas as pd

# Laad je csv
df = pd.read_csv("jouw_data.csv")  # of .xlsx, .json

# Verbinden met database
conn = sqlite3.connect("facturatie.db")
df.to_sql("uren", conn, if_exists="append", index=False)
conn.commit()
conn.close()

print("✅ Import succesvol afgerond.")
