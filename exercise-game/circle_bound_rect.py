import tkinter, random

class Ball:
    pass
class Bar:
    pass

start = False
def pressed(e):
    global start
    if start:
        return
    start = True
    main()

def motion(e):
    bar.x = e.x-bar.w/2
    cvs.coords(bar.id,bar.x,bar.y,
               bar.x+bar.w,bar.y+bar.h)

def colliderect(bar,ball):
    if ball.x+ball.dia>=bar.x and ball.x<=bar.x+bar.w:
        if ball.y+ball.dia>=bar.y and ball.y+ball.dia<=bar.y+bar.h or \
            ball.y<=bar.y+bar.h and ball.y>=bar.y:
            return True
    return False

def main():
    for b in balls:
        b.x += b.dx
        b.y += b.dy
        if b.x < b.dia/2 or b.x > 500-b.dia/2:
            b.dx *= -1
        if b.y < b.dia/2 or b.y > 500-b.dia/2:
            b.dy *= -1
            if b.y > 500-b.dia/2:
                b.c = (b.c+1)%3
                cvs.itemconfig(b.id,fill=colors[b.c])
        if colliderect(bar,b):
            b.dy = -(abs(b.dy))
        cvs.coords(b.id,b.x,b.y,b.x+b.dia,b.y+b.dia)
    root.after(10,main)

root = tkinter.Tk()
root.title('円は四角形に当たったら跳ね返る')
root.bind('<Motion>', motion)
root.bind('<Button>', pressed)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
bar = Bar()
bar.x,bar.y = 220,470
bar.w,bar.h = 60,20
bar.id = cvs.create_rectangle(bar.x,bar.y,
                            bar.x+bar.w,bar.y+bar.h,
                            fill='black',tags='bar')
colors = ['blue','red','cyan']
balls = []
for i in range(3):
    b = Ball()
    b.x = random.randint(100,400)
    b.y = random.randint(100,250)
    b.dx = random.randint(1,3)
    b.dy = random.randint(-3,-1)
    b.dia = 20
    b.c = 0
    b.id = cvs.create_oval(b.x,b.y,
                           b.x+b.dia,b.y+b.dia,
                           fill=colors[b.c],tags='ball')
    balls.append(b)

root.mainloop()