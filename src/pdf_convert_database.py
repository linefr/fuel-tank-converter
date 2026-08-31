import sqlite3
from pdf_extraction import fuel_tanks
import pandas as pd

df = {}

for tank_name, tank_data in fuel_tanks.items():
    df[tank_name] = pd.DataFrame(tank_data)

db_tanks = sqlite3.connect("tanks.db")

