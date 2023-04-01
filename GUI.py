import tkinter as tk


HEIGHT = 700
WIDTH = 1200


root = tk.Tk()



canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

root.title("Carbon Game")
root.mainloop()
