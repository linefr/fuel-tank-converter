from tkinter import *
from receives import receive_cm_tank

# Get centimeters and selected tank
def submit():
    cm = entry.get()
    variable = tank_variable.get()
    if cm.isdigit():
        today = receive_cm_tank(cm, variable)
        # Clear the error message
        text.set(today)
        label.config(font=("Arial", 20))
                                         
    else:
        # Display an error message
        text.set("ERROR")
        label.config(font=("Arial", 80),
                     fg='red' # Change color
        )


tanks = ['15-15-30', '10-10-10-30']
window = Tk()
window.geometry("300x300")

# Text label
text = StringVar(value='')
label = Label(textvariable=text)
label.config(font=("Arial", 2))
label.place(anchor='center',relx=0.5,rely=0.5)

# Convert button
button = Button(window)
button.config(text="Convert", command=submit)
button.place(x=150,y=250,anchor=CENTER)

# User input (centimeters)
entry = Entry(window)
entry.config(font=("Arial", 50))
entry.place(width=300,y=50)

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