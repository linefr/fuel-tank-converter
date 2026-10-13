import sqlite3
from pathlib import Path

def receive_fuels(fuel_name, fuels):
    """
    NOTE: I NEED TO HANDLE THE CASE WHERE CM IS NOT FOUND IN THE DATABASE
    """

    # Using the pathlib library to find the database inside the data folder
    private_directory = Path(__file__).parent.parent / "data"

    databases = list(private_directory.glob("*.db"))

    # DATABASE CONNECTION
    con = sqlite3.connect(databases[0])
    cur = con.cursor()

    cm = fuels[fuel_name]["cm"] 
    tank_variable = fuels[fuel_name]["tank"] 
    if cm is not None and tank_variable is not None:

            cur.execute(
                f'SELECT litres FROM "{tank_variable}" WHERE cm = {cm}'
            )
            result = cur.fetchone()
            if result is None:
                  return None
            else:
                litres = result[0]
                fuels[fuel_name]["litres"] = litres
                return fuels[fuel_name]["litres"]

    con.close()


