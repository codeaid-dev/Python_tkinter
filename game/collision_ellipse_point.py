import tkinter

class Ellipse:
    pass

def motion(e):
    global mx, my
    mx, my = e.x, e.y

def main():
    dx = mx - en.x
    dy = my - en.y
    val = (dx*dx)/(en.rw*en.rw) + (dy*dy)/(en.rh*en.rh)
    if val <= 1:
        cvs.itemconfig(en.id, fill='red')
    else:
        cvs.itemconfig(en.id, fill='black')
    root.after(10, main)

root = tkinter.Tk()
root.title('点と楕円の当たり判定')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
en = Ellipse()
en.rw, en.rh = 100, 200
en.x, en.y = 250, 250
en.id = cvs.create_oval(en.x-en.rw,en.y-en.rh,
                        en.x+en.rw,en.y+en.rh,
                        fill='black',width=0)
mx, my = 0, 0
main()

root.mainloop()