# CM to Litres Converter

A Python application that converts fuel tank measurements from centimetres to litres using calibration data extracted from PDF files and stored in SQLite.

## Project Status

✅ **Development Complete**

The project has reached its initial development goals. It provides a graphical user interface built with Python and Tkinter for converting fuel tank measurements.

### Features

- Select a fuel tank.
- Enter measurements in centimetres.
- Convert centimetres to litres using calibration data.
- Display validation and error messages.
- Store calibration data in SQLite.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/linefr/fuel-tank-converter.git
cd fuel-tank-converter
```

### 2. Set up a virtual environment

Create and activate a Python virtual environment.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the PDF directory

From the project root, create the following directory:

```bash
mkdir -p data/private
```

### 5. Add calibration PDF files

Place the corresponding fuel tank calibration PDF files inside `data/private/`.

These files are required to extract the calibration measurements used by the application.

## Notes

- The application requires valid fuel tank calibration PDF files.
- The `.venv/` and `data/private/` directories should be excluded from version control using `.gitignore`.