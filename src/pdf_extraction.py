import pdfplumber
from pathlib import Path

# Stores the extracted tank data
fuel_tanks = {}

# Path to the directory containing the tank PDF files
private_directory = Path(__file__).parent.parent / "data" / "private"

for file in private_directory.iterdir():
    if file.suffix.lower() == ".pdf":
        with pdfplumber.open(file) as pdf:
            page = pdf.pages[0]
            table = page.extract_table()

            for index, row in enumerate(table):
                # Checks that the item is not None and contains "cm"
                # Pseudocode: the item must not be None, and "cm" must
                # be present in the lowercase version of the item
                # The for loop checks every cell in the row
                if any(
                    item is not None and "cm" in item.lower()
                    for item in row
                ): 
                    number_begin_cm = index
                    length_cm_litres = len(row)
                    break

            tank_name = file.stem

            fuel_tanks[tank_name] = {
                "cm": [],
                "litres": []
            }

            position_cm = range(0, length_cm_litres, 2)

            for position in position_cm:
                for row_cm_litres in table[number_begin_cm + 1:]:
                    cm_value = row_cm_litres[position]
                    litres_value = row_cm_litres[position + 1]

                    if cm_value is None or litres_value is None:
                        continue

                    cm_value = cm_value.strip()
                    litres_value = litres_value.strip()

                    if not cm_value or not litres_value:
                        continue

                    fuel_tanks[tank_name]["cm"].append(cm_value)
                    fuel_tanks[tank_name]["litres"].append(litres_value)

