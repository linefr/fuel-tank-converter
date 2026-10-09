import tkinter as tk
from receives import receive_fuels


"""
Use the 'tk' alias to make Tkinter classes and functions easier to identify
and improve code readability.
"""
# Get centimeters and selected tank

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
    for fuel_name, details_fuels in fuels.items():
        for values in details_fuels.values():

            if values.isdigit():
                fuels["litres"] = receive_fuels(fuel_name, fuels)
                # Clear the error message
            else:
                        # Display an error message
                        text.set("ERROR")
                        label.config(font=("Arial", 80),
                                    fg='red' # Change color
                        )
                
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