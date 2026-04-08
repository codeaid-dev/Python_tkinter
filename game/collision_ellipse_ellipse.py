import tkinter, math

class Ellipse:
    pass

def motion(e):
    en1.cx, en1.cy = e.x, e.y
    cvs.coords(en1.id, en1.cx-en1.rw,en1.cy-en1.rh,
            en1.cx+en1.rw,en1.cy+en1.rh)

def main():
    if collision(en1, en2):
        cvs.itemconfig(en2.id, fill='red')
    else:
        cvs.itemconfig(en2.id, fill='black')
    root.after(10, main)

def collision(e1, e2):
    for i in range(0, 360, 5):
        t = i * (math.pi / 180)
        # e1の境界点
        ex = e1.cx + e1.rw * math.cos(t)
        ey = e1.cy + e1.rh * math.sin(t)
        # e2中心までの距離
        dx = ex - e2.cx
        dy = ey - e2.cy
        # e2の中に入っているかチェック
        if (dx*dx)/(e2.rw*e2.rw) + (dy*dy)/(e2.rh*e2.rh) <= 1:
            return True

    return False

root = tkinter.Tk()
root.title('楕円と楕円の当たり判定')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
en1 = Ellipse()
en1.rw, en1.rh = 100, 50
en1.cx, en1.cy = 100, 50
en1.id = cvs.create_oval(en1.cx-en1.rw,en1.cy-en1.rh,
                        en1.cx+en1.rw,en1.cy+en1.rh,
                        fill='green',width=0)
en2 = Ellipse()
en2.rw, en2.rh = 50, 100
en2.cx, en2.cy = 250, 250
en2.id = cvs.create_oval(en2.cx-en2.rw,en2.cy-en2.rh,
                        en2.cx+en2.rw,en2.cy+en2.rh,
                        fill='black',width=0)
main()

root.mainloop()