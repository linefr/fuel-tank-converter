from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("first GUI program")

label = Label(window, text = "HELLO",font=('Arial',21,'bold'), fg='grey')
label.pack()

window.mainloop()