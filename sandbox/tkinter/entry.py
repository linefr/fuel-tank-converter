from tkinter import *
from receives import receive_cm_tank

# Get centimeters and selected tank
def submit():
    cm = entry.get()
    variable = tank_variable.get()
    if cm.isdigit():
        receive_cm_tank(cm, variable)

        # Clear the error message
        text.set("")
        label.config(font=("Arial", 20))
                                         
    else:
        # Display an error message
        text.set("ERROR")
        label.config(font=("Arial", 100),
                     fg='red' # Change color
        )


tanks = ['15-15-30', '10-10-10-30']
window = Tk()

# Text label
text = StringVar(value='')
label = Label(textvariable=text)
label.config(font=("Arial", 20))
label.pack()

# Convert button
button = Button(window)
button.config(text="Convert", command=submit)
button.pack()

# User input (centimeters)
entry = Entry(window)
entry.config(font=("Arial", 50))
entry.pack()

# User input (tank selection)

# Variable
tank_variable = IntVar()

for index in range(len(tanks)):
    radiobutton = Radiobutton(
        window,
        text=tanks[index],
        variable=tank_variable,
        value=index
    )
    radiobutton.pack()

window.mainloop()