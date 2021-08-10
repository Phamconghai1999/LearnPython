from tkinter import *


root = Tk()

root.geometry("300x150+200+200")
root.title("Text Box")

tbx_1 = Entry(root,width=45)
tbx_1.place(x=10,y=20)

lbl_1 = Label(root, text ="")
lbl_1.place(x=10, y=80)

def ok_clicked():
    data = tbx_1.get() # doi tuong dang chuoi string 
    #check 
    for a in data:
        if (a.isnumeric() == True):
            lbl_1.configure(text="Co so trong day")
            break
    else:
        lbl_1.configure(text=data)

    

ok_btn = Button(root,text ="OK",command=ok_clicked)
ok_btn.place(x=250,y=50)

#check number in textbox.



root.mainloop()