import tkinter as tk
color = "black"
def draw(event):
    canvas.create_oval(event.x - 4, event.y - 4, event.x + 4, event.y + 4,
                       fill=color, outline=color)
def set_color(new_color):
    global color
    color = new_color
def clear():
    canvas.delete("all")
root = tk.Tk()
root.title("Тақта")
canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.pack()
canvas.bind("<B1-Motion>", draw)
tk.Button(root, text="Қара", command=lambda: set_color("black")).pack(side="left")
tk.Button(root, text="Қызыл", command=lambda: set_color("red")).pack(side="left")
tk.Button(root, text="Көк", command=lambda: set_color("blue")).pack(side="left")
tk.Button(root, text="Өшіргіш", command=lambda: set_color("white")).pack(side="left")
tk.Button(root, text="Тазалау", command=clear).pack(side="left")
root.mainloop()
