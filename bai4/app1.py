from tkinter import *


def callback(sv):
    lbl_1.configure(text=sv.get())

window = Tk()
window.geometry("300x150+200+200")
window.title("Text Box")

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
#tbx_1 = Entry(window,width=45)
tbx_1 = Entry(window, textvariable=sv,width=45)
tbx_1.place(x=10,y=20)

lbl_1 = Label(window, text ="")
lbl_1.place(x=10, y=80)

window.mainloop()