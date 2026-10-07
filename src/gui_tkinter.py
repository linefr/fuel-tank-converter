import tkinter as tk
from receives import receive_cm_tank


"""
Use the 'tk' alias to make Tkinter classes and functions easier to identify
and improve code readability.
"""
# Get centimeters and selected tank

def submit():
    cm = entry.get()
    variable = tank_variable.get()
    if cm.isdigit():
        measurements = receive_cm_tank(cm, variable)

        # Clear the error message
        show_results(measurements)
        label.config(font=("Arial", 20))
                                         
    else:
        # Display an error message
        text.set("ERROR")
        label.config(font=("Arial", 80),
                     fg='red' # Change color
        )

def show_results(measurements):
   
    result_window = tk.Toplevel(window)
    for tank, cm_litres in measurements.items():
                results = tk.Label(
                    result_window,
                    text=f'{tank}:{cm_litres['cm']} cm - {cm_litres['litres']}L'
                )
                results.pack()
                
    


tanks = ['15-15-30', '10-10-10-30']
window = tk.Tk()
window.geometry("300x300")

# Text label
text = tk.StringVar(value='')
label = tk.Label(textvariable=text)
label.config(font=("Arial", 2))
label.place(anchor='center',relx=0.5,rely=0.5)

# Convert button
button = tk.Button(window)
button.config(text="Convert", command=submit)
button.place(x=150,y=250,anchor=tk.CENTER)

# User input (centimeters)
entry = tk.Entry(window)
entry.config(font=("Arial", 50))
entry.place(width=300,y=50)

# User input (tank selection)

# Variable
tank_variable = tk.IntVar()

for index in range(len(tanks)):
    radiobutton = tk.Radiobutton(
        window,
        text=tanks[index],
        variable=tank_variable,
        value=index
    )
    radiobutton.pack()

window.mainloop()