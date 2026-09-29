import sqlite3
from pathlib import Path


def execute_database(cm, tank_variable):
    """
    NOTE: I NEED TO HANDLE THE CASE WHERE CM IS NOT FOUND IN THE DATABASE
    """

    # Using the pathlib library to find the database inside the data folder
    private_directory = Path(__file__).parent.parent.parent / "data"

    databases = list(private_directory.glob("*.db"))
    print(databases)

    # DATABASE CONNECTION
    con = sqlite3.connect(databases[0])
    cur = con.cursor()

    print(cm)
    print(tank_variable)

    if cm is not None and tank_variable is not None:
        cur.execute(
            f'SELECT litres FROM "{tank_variable}" WHERE cm = {cm}'
        )
        result = cur.fetchone()

        # RESULT IN LITRES
        litres = result[0]
        print(litres)

    con.close()


def receive_cm_tank(cm, tank_variable):
    if cm.isdigit():
        if tank_variable == 0:
            tank_variable = '15-15-30'
        elif tank_variable == 1:
            tank_variable = '10-10-10-30'
        else:
            print("ERROR")

        if tank_variable in ('15-15-30', '10-10-10-30'):
            return execute_database(cm, tank_variable)
    else:
        print('This text is not a digit')