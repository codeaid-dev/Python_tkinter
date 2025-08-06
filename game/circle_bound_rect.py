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
    if ball.x < bar.x:
        closestX = bar.x
    elif ball.x > bar.x + bar.w:
        closestX = bar.x + bar.w
    else:
        closestX = ball.x
    
    if ball.y < bar.y:
        closestY = bar.y
    elif ball.y > bar.y + bar.h:
        closestY = bar.y + bar.h
    else:
        closestY = ball.y
    
    dx = ball.x - closestX
    dy = ball.y - closestY
    distance = (dx**2 + dy**2)**0.5
    return distance < ball.r

def main():
    for b in balls:
        b.x += b.dx
        b.y += b.dy
        if b.x < b.r or b.x > 500-b.r:
            b.dx *= -1
        if b.y < b.r or b.y > 500-b.r:
            b.dy *= -1
            if b.y > 500-b.r:
                b.c = (b.c+1)%3
                cvs.itemconfig(b.id,fill=colors[b.c])
        if colliderect(bar,b):
            b.dy = -(abs(b.dy))
        cvs.coords(b.id,b.x-b.r,b.y-b.r,b.x+b.r,b.y+b.r)
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
    b.r = 10
    b.c = 0
    b.id = cvs.create_oval(b.x-b.r,b.y-b.r,
                           b.x+b.r,b.y+b.r,
                           fill=colors[b.c],
                           tags='ball',width=0)
    balls.append(b)

root.mainloop()