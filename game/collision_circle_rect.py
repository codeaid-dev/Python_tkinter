import tkinter

class Circle:
    pass
class Rectangle:
    pass

def motion(e):
    p.x = e.x
    p.y = e.y
    cvs.coords(p.id,p.x-p.r,p.y-p.r,p.x+p.r,p.y+p.r)

def collision(rect,circle):
    if circle.x < rect.x:
        closestX = rect.x
    elif circle.x > rect.x + rect.w:
        closestX = rect.x + rect.w
    else:
        closestX = circle.x

    if circle.y < rect.y:
        closestY = rect.y
    elif circle.y > rect.y + rect.h:
        closestY = rect.y + rect.h
    else:
        closestY = circle.y

    dx = circle.x - closestX
    dy = circle.y - closestY
    distance = (dx**2 + dy**2)**0.5
    return distance < circle.r

def main():
    if collision(r, p):
        cvs.itemconfig(r.id,fill='red')
    else:
        cvs.itemconfig(r.id,fill='black')
    root.after(10, main)

root = tkinter.Tk()
root.title('円と矩形(四角形)の当たり判定')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
p = Circle()
p.x, p.y, p.r = 50, 50, 50
p.id = cvs.create_oval(p.x-p.r,p.y-p.r,
                           p.x+p.r,p.y+p.r,
                           fill='green',
                           tags='circle',width=0)
r = Rectangle()
r.x, r.y = 200, 200
r.w, r.h = 100, 100
r.id = cvs.create_rectangle(r.x,r.y,
                            r.x+r.w,r.y+r.h,
                            fill='black', width=0)
main()
root.mainloop()
