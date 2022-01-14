from tkinter import Tk, Canvas, YES, BOTH, mainloop

ws = Tk()
ws.title('xxxxxxx')

mul = 10
width=10*mul
height=10*mul

canvas = Canvas(
    ws,
    width=width,
    height=height
)
canvas.pack(expand=YES, fill=BOTH)

def Draw_point(x, y, size = 2):
    python_green = "#476042"
    x1, y1 = (x - 1*size) + width/2, (y - 1*size) + height/2
    x2, y2 = (x + 1*size) + width/2, (y + 1*size) + height/2
    canvas.create_oval(x1, y1, x2, y2, fill="#476042")

def Run(run=True):
    if(run):
        mainloop()

if __name__ == "__main__":
    Draw_point(0, 0)
    Run()