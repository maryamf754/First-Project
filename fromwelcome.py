from tkinter import *
root=Tk()
root.geometry('300x300')
root.config(bg="#c9b5c3")
def open_window():
    win=Toplevel(root)
    #پنجره جدید(فرزند  پنجره اصلی)  یا ساختن پنجره جدا
    win.title("new window")
    win.geometry("300x200")
    win.config(bg="#a8c8b9")
   # win.iconbitmap("map.ico")
    #تلاش می کنه ایکون پنجره جدید  را با فایل تنظیم کنه 
    #حتما ایکون دانلود می کنیم و توی عکس  برنامه  تو فایل پروزه قرار می دهیم
    Label(win,text=" خوش امدید", font=("arial",16)).pack(pady=20)
Button(root,text="بازکردن پنجره خوش امدید", command=open_window ,font=("arial",12)).pack(pady=50)

root.mainloop()