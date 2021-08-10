from tkinter import *
from tkinter.ttk import Style

window = Tk(); #class Tk create window, always create window before create widget
window.geometry("250x350+1200+200")
window.title("Khai bao y te")

lbl_name = Label(window, text ="Name: ")
lbl_name.place(x=0, y=10)
tbx_name = Entry(window, text ="",width=25)
tbx_name.place(x=50, y=10)

lbl_date = Label(window, text ="Date: ")
lbl_date.place(x=0, y=35)
tbx_date = Entry(window,width=5)
tbx_date.place(x= 50, y=35)
tbx_month = Entry(window,width=5)
tbx_month.place(x= 100, y=35)
tbx_year = Entry(window,width=10)
tbx_year.place(x= 150, y=35)

varSexual = StringVar()
lbl_Sex = Label(window, text ="Sex: ")
lbl_Sex.place(x=0, y=60)
M_opt = Radiobutton(window, text ="Male",variable=varSexual ,value = "Male")
M_opt.place(x=50, y=60)
F_opt = Radiobutton(window, text ="Female",variable=varSexual ,value = "Female")
F_opt.place(x=150, y=60)

lbl_Error = Label(window, text ="")
lbl_Error.place(x=0,y=120)

lbl_ShowName = Label(window, text ="Name: ")
lbl_ShowName.place(x=0,y=200)
lbl_ShowDateofBirth = Label(window, text ="Date of birth: ")
lbl_ShowDateofBirth.place(x=0,y=225)
lbl_ShowAge = Label(window, text ="Age: ")
lbl_ShowAge.place(x=0,y=250)
lbl_ShowSexual = Label(window, text ="Sexual: ")
lbl_ShowSexual.place(x=0,y=275)

def ShowErr(str):
    lbl_Error.configure(text = str)

def OK_clicked():
    _Name = tbx_name.get()
    _Date = tbx_date.get()
    _Month = tbx_month.get()
    _Year = tbx_year.get()

    if (_Name == ""):
        ShowErr("Name Empty")
    elif (_Name.isnumeric()==True):
        ShowErr("Name Error")
    else:
        Name = _Name
        lbl_ShowName.configure(text = "Name: " + Name)
        #ShowErr("")
        if (_Date=="" or _Month=="" or _Year==""):
            ShowErr("Date of birth Empty")
        if (_Date.isnumeric()==False or _Month.isnumeric()==False or _Year.isnumeric()==False):
            ShowErr("Date must be numeric")
        else:
            
            lbl_ShowDateofBirth.configure(text = "Date of birth: " + _Date + "/" + _Month + "/" + _Year)
            Age = 2021 - int(_Year) + 1
            lbl_ShowAge.configure(text= "Age: " + str(Age))
            #ShowErr("")
            if (varSexual.get() == ""):
                ShowErr("Pls choice sexual")
            else:
                lbl_ShowSexual.configure(text = "Sexual: " + varSexual.get())
                Sexual = varSexual.get()
                ShowErr("Ready")
                saveButton.place(x=200,y=300)

onButton = Button(window,text="OK", command = OK_clicked, borderwidth=2)
onButton.place(x=200, y=120)
def SaveData():
    if  (lbl_Error.cget("text") == "Ready"):
        dataFile = open('data.txt', 'a')
        Name = tbx_name.get()
        DoB = tbx_date.get() + tbx_month.get() + tbx_year.get()
        Age = 2021 - int(tbx_year.get()) + 1
        Sexual = varSexual.get()
        data = {
            'name': Name,
            'date': DoB,
            'sexual': Sexual,
            'age': Age
        }
        dataFile.write(str(data))
        dataFile.write("\n")
        dataFile.close()
        ShowErr("Saved")
        saveButton.place_forget()

saveButton =Button(window,text="SAVE", command=SaveData)



window.mainloop()

#