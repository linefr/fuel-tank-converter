from tkinter import *
from receives_cm import receive_cm


# Get centimeters
def submit():
    cm = entry.get()
    receive_cm(cm)


window = Tk()

# Convert button
button = Button(window)
button.config(text="Convert", command=submit)
button.pack()

# User input (centimeters)
entry = Entry(window)
entry.config(font=("Arial", 50))
entry.pack()

window.mainloop()