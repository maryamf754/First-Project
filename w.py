from tkinter import *
import random
win=Tk()
win.geometry("400x300")
def change_color(event):

    code=[chr(i) for  i  in range(65,71)] + [str(i) for i in range(0,10)]
    color_list=random.choices(code,k=6)
    color_hex='#' + ''.join(color_list)
    win.config(bg=color_hex)

win.focus_set()
#win.bind('<Button-3>',change_color)

#win.bind('<key>',change_color)
#win.bind('<Up>',change_color)
#win.bind('<Down>',change_color)
#win.bind('Left>',change_color)
#win.bind('<Down>',change_color)
#win.bind('<Shift-Button-1>',change_color)
win.bind('<a>',change_color)
win.mainloop()