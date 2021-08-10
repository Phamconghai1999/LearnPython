from tkinter import *

#khoi tao cua so window

window  = Tk() 
window.title("Tinh tong") #thuoc tinh
window.geometry("300x300")

#tao nhan Label
lbl_1 = Label(window, text="So thu 1:") # khoi tao doi tuong label
lbl_1.grid(column=0, row=0) #thuoc tinh

#tao textbox de nhap so vao
txt_1 = Entry(window,width=20)
txt_1.grid(column=1, row=0)

#tao nhan Label
lbl_2 = Label(window, text="So thu 2:") # khoi tao doi tuong label
lbl_2.grid(column=0, row=1) #thuoc tinh

#tao textbox de nhap so vao
txt_2 = Entry(window,width=20)
txt_2.grid(column=1, row=1)

#tao nhan Label
lbl_3 = Label(window, text="Tong:") # khoi tao doi tuong label
lbl_3.grid(column=0, row=3) #thuoc tinh

lbl_4 = Label(window, text=" ") # khoi tao doi tuong label
lbl_4.grid(column=1, row=4) #thuoc tinh

#ham duoc goi khi bam nut
def clicked():
    Tb1_Str = txt_1.get()
    Tb2_Str = txt_2.get()
    if ((Tb1_Str.isnumeric() == False) or (Tb2_Str.isnumeric()== False)): #methode
        lbl_4.configure(text="Loi ki tu")
    else:
        SUM = int(Tb1_Str) + int(Tb2_Str)
        lbl_4.configure(text=SUM)
    return

#tao 1 button:
btn = Button(window,text="Tinh", command=clicked)
btn.grid(column=0, row=2)



window.mainloop()

#bai tap
# kiem tra 2 ô nhập dữ liệu, nếu k hông phải chữ số thì hiện thông báo lỗi bên dưới
