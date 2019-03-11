from tkinter import *

root = Tk()

txt = "成人限制！\n十八禁！"
textLabel = Label(root, \
					text=txt,
					justify=LEFT, padx=10)
textLabel.pack(side = LEFT)

photo = PhotoImage(file = "18.gif")
imgLable = Label(root, image = photo)
imgLable.pack(side = RIGHT)

mainloop()