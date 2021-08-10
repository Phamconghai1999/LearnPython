from tkinter import *

window  = Tk()
window.title("QTT PY TEST")
window.geometry("400x400")

btnOpen = Button(window, text = "Mwo mwo")
btnOpen.grid(column=2, row=1)
btnClose = Button(window, text = "Close")
btnClose.grid(column=2, row=2)
lbData = Label(window, text="Bla bLa bla")
lbData.grid(column=0, row=0)

window.mainloop()
