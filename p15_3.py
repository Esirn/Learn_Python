from tkinter import *

root = Tk()

txt = "成人限制！十八禁！"
textLabel = Label(root, text=txt)
textLabel.pack(side = LEFT)

photo = PhotoImage(file = "18.gif")
imgLable = Label(root, image = photo)
imgLable.pack(side = RIGHT)