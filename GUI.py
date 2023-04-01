import tkinter as tk


HEIGHT = 700
WIDTH = 1200


root = tk.Tk()

#this is just here to reserve the space on the gui
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

gameFrame = tk.Frame(root, bg="#f4f1e4")
gameFrame.place(relheight=1, relwidth=0.8, relx = 0.2, rely=0)

actionBar = tk.Frame(root, bg="#efe9d4")
actionBar.place(relheight=1, relwidth=0.2, relx=0, rely=0)

root.title("Carbon Game")
root.mainloop()
