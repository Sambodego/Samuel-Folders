from tkinter import *
import snakegame
import ponggame


root = Tk()

def function1():
    print("Menu item clicked")

    

def endProgram():
    root.destroy()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
submenu.add_command(label="Snake Game", command= snakegame.game)
submenu.add_command(label="Ping pong", command= ponggame.game)
#submenu.add_command(label="Ping Pong", command= function1)

submenu.add_separator()
submenu.add_command(label="Exit", command=endProgram)
submenu.add_command(label="Project", command=function1)
submenu.add_command(label="Save", command=function1)


newmenu = Menu(mymenu)
#mymenu.add_cascade(label="Edit")
#newmenu = Menu(mymenu)
mymenu.add_cascade(label="Files", menu=newmenu)
newmenu.add_command(label="Game Data", command=function1)
newmenu.add_command(label="Reset Data", command=function1)


root.mainloop()



















 