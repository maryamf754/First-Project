from tkinter import *
root=Tk()
root.geometry('300x300')
def open_window():
    win=Toplevel(root)
    #پنجره جدید(فرزند  پنجره اصلی)  یا ساختن پنجره جدا
    win.title("new window")
    win.geometry("300x200")
    win.iconbitmap("icon.ico")
    #تلاش می کنه ایکون پنجره جدید  را با فایل تنظیم کنه 

Button(root,text="open", command=open_window).pack()

root.mainloop()