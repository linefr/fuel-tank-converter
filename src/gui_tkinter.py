import tkinter as tk
from receives import receive_fuels


class FuelConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Tank Converter")
        self.root.geometry("350x350")
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
        # Inicialize variable text
        self.text_var = tk.StringVar(value="Initial Text")
        button = tk.Button(self.root)
        button.config(text="Convert", command=self.submit)
        button.grid(row=10)


    def submit(self):
        fuels = self.get_fuels()

        if not self.validate_fuels(fuels):
            self.show_error()
            return

        fuels = self.convert_fuels(fuels)
        # Updat the value inside StringVar
        self.text_var.set(self.print_text(fuels))
        self.show_results(fuels)


    def print_text(self, fuels):
        text = ''
        for fuel, details in fuels.items():
            text += f'{f'{fuel}:':^24}\n'
            for properties, properties_values in details.items():
                text += f'{properties + " -":<12}{str(properties_values):>12}\n'
            text += "-" * 22 + "\n" 
            
        return text
            

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
        for details in fuels.values():
            # Trabalhar no sentido inverso, tentar pelo nao
            if not details["cm"].isdigit():
                return False

        return True

    def convert_fuels(self, fuels):
        for fuel_name, details_fuels in fuels.items():
            details_fuels["litres"] = receive_fuels(fuel_name, fuels)
        return fuels

    def show_error(self):
        # New window no references with main window
        error_window = tk.Toplevel(self.root)
        error_window.title("ERROR")
        error_window.geometry("200x100")
        label_error = tk.Label(
            error_window,
            text = "Please enter valid number.",
            fg='red'
            )
        label_error.pack(pady=25)

        # Closing error mensagem 
        button = tk.Button(
            error_window,
            text="Close",
            command=error_window.destroy
        )
        button.pack()

    def show_results(self, fuels):
        results_window = tk.Toplevel(self.root)
        results_window.title("Results")
        results_window.geometry("210x420")
        text_widget = tk.Text(
                    results_window,
                    width=35,
                    height=25,
                    font=("Menlo", 12),
                    wrap="none"
                )
        text_widget.insert("1.0", self.text_var.get())
        text_widget.config(state="disabled")
        text_widget.pack(padx=10, pady=10)




root = tk.Tk()
app = FuelConverterApp(root)

root.mainloop()

