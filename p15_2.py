import tkinter as tk

class App:
	def __init__(self,root):
		frame = tk.Frame(root)
		frame.pack(side=tk.LEFT, padx=10, pady=10)
		self.hi_there = tk.Button(frame , text="打招呼" , bg="black", fg="white" , command=self.say_hi)
		self.hi_there.pack()
		
	def say_hi(self):
		print("Hello Everyone!")
		
root = tk.Tk()
app = App(root)

root.mainloop()
