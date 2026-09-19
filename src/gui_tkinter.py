# Learning how to use Tkinter

import tkinter as tk


# Main window
root = tk.Tk()
root.title("Convert from cm to litres")


def show():
    variable = entry.get()

    variable_label = tk.Label(root, text=variable)
    variable_label.pack()


# Widget placed inside the root window
label = tk.Label(root, text="What's the measurement in cm?")

# Input field
entry = tk.Entry(root)

# Pass the function to Tkinter.
# Tkinter calls it when the user clicks the button.
button = tk.Button(
    root,
    text="Convert",
    width=25,
    command=show
)

# Position the widgets in the window
label.pack(padx=20, pady=20)
entry.pack()
button.pack()

# Start the event loop
root.mainloop()