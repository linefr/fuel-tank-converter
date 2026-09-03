import sqlite3
from pdf_extraction import fuel_tanks
import pandas as pd
from pathlib import Path

# Re-use: Path to the directory containing the database
private_directory = Path(__file__).parent.parent / "data"

df = {}

for tank_name, tank_data in fuel_tanks.items():
    df[tank_name] = pd.DataFrame(tank_data)

db_tanks = sqlite3.connect(f"{private_directory}/example_tank.db")

for name_tank,tank in df.items():
    tank.to_sql(name_tank,db_tanks,index = False)

db_tanks.close()
