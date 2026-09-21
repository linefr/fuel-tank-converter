from tkinter import *

count = 0

def click():
    global count
    count+=1
    label.config(text=count)

window = Tk()
# Button
button = Button(window,text = "CLICK ME")
button.config(command=click)
button.pack()
# Label
label = Label(window,text=count)
label.config(font=('Arial',50))
label.pack()

window.mainloop()