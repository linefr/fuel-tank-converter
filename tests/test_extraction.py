from pathlib import Path
import sys

directory = Path(__file__).parents[1]/"src"
# Access Python's module search paths through sys.path
# Insert the src directory at index 0
sys.path.insert(0, str(directory))

import pdf_extraction


def test_cm_litres():
    # Check whether each centimetre value has a corresponding litres value
    fuel_tanks = pdf_extraction.fuel_tanks
    for tank in fuel_tanks.values():
        assert len(tank["cm"]) == len(tank["litres"])

