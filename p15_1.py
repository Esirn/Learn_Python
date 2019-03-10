import tkinter as tk

root = tk.Tk()  # 创建主窗口，容纳整个GUI程序。
root.title = ("Demo")  # 设置主窗口对象的标题栏。

theLabel = tk.Label(root , text="The 2nd window!")  # 添加Label组件，可以显示文本、图表和图片。
theLabel.pack()  # 用于自动调节组件本身的尺寸。

root.mainloop()  # 进入主事件循环。