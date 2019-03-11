from tkinter import *

root = Tk()

txt = "成人限制！\n十八禁！"
photo = PhotoImage(file = "18.gif")

theLabel = Label(root, text=txt,
				 justify=LEFT,
				 image=photo,
				 compound=CENTER,
				 font=("华康少女字体", 20),
				 fg="white")
theLabel.pack()

mainloop()
