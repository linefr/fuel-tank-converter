import tkinter as tk
from receives import receive_fuels


"""
Use the 'tk' alias to make Tkinter classes and functions easier to identify
and improve code readability.
"""
# Get centimeters and selected tank
"""
def submit():
    regular_gasoline = regular_gasoline_entry.get()
    additive_gasoline = additive_gasoline_entry.get()
    diesel_s10 = diesel_s10_entry.get()
    diesel_s500 = diesel_s500_entry.get()
    ethanol = ethanol_entry.get()
    # Combustivel
    fuels = {
    "regular_gasoline": {
        "cm": regular_gasoline,
        "litres": None,
        "tank": "15-15-30"
    },
    "additive_gasoline": {
        "cm": additive_gasoline,
        "litres": None,
        "tank": "10-10-10-30"
    },
    "diesel_s10": {
        "cm": diesel_s10,
        "litres": None,
        "tank": "15-15-30"
    },
    "diesel_s500": {
        "cm": diesel_s500,
        "litres": None,
        "tank": "15-15-30"
    },
    "ethanol": {
        "cm": ethanol,
        "litres": None,
        "tank": "10-10-10-30"
    }
    }
    # Is get error?
    error_mensagem = False
    for fuel_name, details_fuels in fuels.items():

        cm = details_fuels['cm']

        if cm.isdigit():
            details_fuels["litres"] = receive_fuels(fuel_name, fuels)
        # Clear the error message
        else:
            error_mensagem = True
            break
            

    if error_mensagem:
        window.destroy()
    else:
                
        text.set(fuels)
        label.config(font=("Arial", 20))

                                            
                



tanks = ['15-15-30', '10-10-10-30']
window = tk.Tk()
window.geometry("400x400")

# Clean and designs cms
input_frame = tk.LabelFrame(
    window,
    text="Fuel Measurements",
    padx=20,
    pady=20
)
input_frame.grid(row=0, column=0, padx=20, pady=20)

error_window = tk.Tk()
error_frame = tk.LabelFrame(
    error_window,
    text="ERROR"
)

# New Window
tk.Label(
    input_frame,
    text="Regular Gasoline"
).grid(row=0, column=0, sticky="w", pady=8)

# Text label
text = tk.StringVar(value='')
label = tk.Label(textvariable=text)
label.config(font=("Arial", 2))
label.grid(row=0, column=0, sticky="w", pady=8)

# Convert button
button = tk.Button(window)
button.config(text="Convert", command=submit)
button.grid(row=10)

# User input (centimeters)
# Fuel measurement inputs

regular_gasoline_entry =tk.Entry(input_frame, width=15)
regular_gasoline_entry.grid(row=0, column=1, padx=10, pady=8)

tk.Label(input_frame, text="Additive Gasoline").grid(
    row=1, column=0, sticky="w", pady=8
)
additive_gasoline_entry = tk.Entry(input_frame, width=15)
additive_gasoline_entry.grid(row=1, column=1, padx=10, pady=8)

tk.Label(input_frame, text="Diesel S10").grid(
    row=2, column=0, sticky="w", pady=8
)
diesel_s10_entry = tk.Entry(input_frame, width=15)
diesel_s10_entry.grid(row=2, column=1, padx=10, pady=8)

tk.Label(input_frame, text="Diesel S500").grid(
    row=3, column=0, sticky="w", pady=8
)
diesel_s500_entry = tk.Entry(input_frame, width=15)
diesel_s500_entry.grid(row=3, column=1, padx=10, pady=8)

tk.Label(input_frame, text="Ethanol").grid(
    row=4, column=0, sticky="w", pady=8
)
ethanol_entry = tk.Entry(input_frame, width=15)
ethanol_entry.grid(row=4, column=1, padx=10, pady=8)




window.mainloop()

"""
class FuelConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Tank Converter")
        self.root.geometry("400x400")
        self.create_fuel_widgets()

    def create_fuel_widgets(self):
        input_frame = tk.LabelFrame(
            self.root,
            text="Fuel Measurements",
            padx=20,
            pady=20,
        )
        input_frame.grid(row=0, column=0, padx=20, pady=20)

        tk.Label(
            input_frame,
            text="Regular Gasoline",
        ).grid(row=0, column=0, sticky="w", pady=8)

        self.regular_gasoline_entry = tk.Entry(input_frame, width=15)
        self.regular_gasoline_entry.grid(
            row=0, column=1, padx=10, pady=8
        )

        tk.Label(
            input_frame,
            text="Additive Gasoline",
        ).grid(row=1, column=0, sticky="w", pady=8)

        self.additive_gasoline_entry = tk.Entry(input_frame, width=15)
        self.additive_gasoline_entry.grid(
            row=1, column=1, padx=10, pady=8
        )

        tk.Label(
            input_frame,
            text="Diesel S10",
        ).grid(row=2, column=0, sticky="w", pady=8)

        self.diesel_s10_entry = tk.Entry(input_frame, width=15)
        self.diesel_s10_entry.grid(
            row=2, column=1, padx=10, pady=8
        )

        tk.Label(
            input_frame,
            text="Diesel S500",
        ).grid(row=3, column=0, sticky="w", pady=8)

        self.diesel_s500_entry = tk.Entry(input_frame, width=15)
        self.diesel_s500_entry.grid(
            row=3, column=1, padx=10, pady=8
        )

        tk.Label(
            input_frame,
            text="Ethanol",
        ).grid(row=4, column=0, sticky="w", pady=8)

        self.ethanol_entry = tk.Entry(input_frame, width=15)
        self.ethanol_entry.grid(
            row=4, column=1, padx=10, pady=8
        )

        button = tk.Button(self.root)
        button.config(text="Convert", command=self.submit)
        button.grid(row=10)

    def submit(self):
        fuels = self.get_fuels()

        if not self.validate_fuels(fuels):
            self.show_error()
            return

        self.convert_fuels(fuels)
        self.show_results(fuels)

    def get_fuels(self):
        # Variables
        regular_gasoline = self.regular_gasoline_entry.get()
        additive_gasoline = self.additive_gasoline_entry.get()
        diesel_s10 = self.diesel_s10_entry.get()
        diesel_s500 = self.diesel_s500_entry.get()
        ethanol = self.ethanol_entry.get()
        # Combustivel
        self.fuels = {
        "regular_gasoline": {
            "cm": regular_gasoline,
            "litres": None,
            "tank": "15-15-30"
        },
        "additive_gasoline": {
            "cm": additive_gasoline,
            "litres": None,
            "tank": "10-10-10-30"
        },
        "diesel_s10": {
            "cm": diesel_s10,
            "litres": None,
            "tank": "15-15-30"
        },
        "diesel_s500": {
            "cm": diesel_s500,
            "litres": None,
            "tank": "15-15-30"
        },
        "ethanol": {
            "cm": ethanol,
            "litres": None,
            "tank": "10-10-10-30"
        }
        }
        return self.fuels
    def validate_fuels(self, fuels):
        for fuel_name, details_fuels in self.fuels.items():
        
                cm = details_fuels['cm']
        
                if cm.isdigit():
                    details_fuels["litres"] = receive_fuels(fuel_name, fuels)
                # Clear the error message
                else:
                    self.show_error()
                    break

    def convert_fuels(self, fuels):
        pass

    def show_error(self):
        pass

    def show_results(self, fuels):
        pass

root = tk.Tk()
app = FuelConverterApp(root)
root.mainloop()