from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
win = Tk()
win.title("Your Text Editor")
win.geometry('500x500')
def show():
    f = filedialog.askopenfilename(filetypes=(("Text File","*.txt"),("all files","*.*")))

def showsave():
    filedialog.asksaveasfile()

def new():
    subw =Toplevel()
    subw.geometry("400x400")
    subw.title("New Window")
    menu()
    t2=Text(subw)
    t2.pack()

def callback():
    result = askcolor(color="#6A9662")
    win.config(bg=result[-1])


def menu():
    mb = Menu(win)
    filemenu = Menu(mb , tearoff=0)
    filemenu.add_command(label="New",command=new)
    filemenu.add_separator()
    filemenu.add_command(label="Open",command=show)
    filemenu.add_separator()
    filemenu.add_command(label="Save",command=showsave)
    filemenu.add_separator()
    filemenu.add_command(label="Print")
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quit)
    filemenu.add_separator()
    mb.add_cascade(label = "File",menu=filemenu)
    editmenu = Menu(mb,tearoff=0)
    editmenu.add_command(label="Cut" )
    editmenu.add_separator()
    editmenu.add_command(label="Copy")
    editmenu.add_separator()
    editmenu.add_command(label="Paste")
    editmenu.add_separator()
    editmenu.add_command(label="Color",command=callback)
    editmenu.add_separator()
    mb.add_cascade(label="Edit",menu=editmenu)
    win.config(menu=mb)
    t1=Text(win)
    t1.pack()

menu()

win.mainloop()
