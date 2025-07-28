import tkinter,random, time

class Circle:
    def __init__(self):
        self.x = random.randint(0,450)
        self.y = random.randint(0,450)
        self.dx = random.randint(1,5)
        self.dy = random.randint(1,5)
        self.interval = random.randint(1,100)

circles = []
start = None
finish = False

def pressed(event):
    global finish
    count = 0
    for ball in circles:
        dist = ((ball.x+25-event.x)**2+(ball.y+25-event.y)**2)**0.5
        if dist < 25:
            ball.dx = 0
            ball.dy = 0
            ball.interval = 0
    for ball in circles:
        if ball.interval == 0:
            count += 1
    if count == len(circles) and not finish:
        finish = True
        spend = time.time() - start
        cvs.create_text(250,250,text=f'経過時間: {spend:.0f}秒',fill='red',font=('Helvetica',40))

def main():
    if finish:
        return
    for ball in circles:
        ball.x += ball.dx
        ball.y += ball.dy
        if ball.x > 450 or ball.x < 0:
            ball.dx *= -1
        if ball.y > 450 or ball.y < 0:
            ball.dy *= -1

        if ball.interval != 0:
            ball.interval += 1

        if ball.interval != 0 and ball.interval % 100 == 0:
            nx = random.randint(0,450)
            ny = random.randint(0,450)
            ball.dx = (nx-ball.x)/40
            ball.dy = (ny-ball.y)/40
        cvs.coords(ball.id,ball.x,ball.y,ball.x+50,ball.y+50)

    root.after(10,main)

root = tkinter.Tk()
root.title('ランダムに動く複数の円をクリック')
root.bind('<Button>', pressed)
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
for i in range(4):
    ball = Circle()
    ball.id = cvs.create_oval(ball.x,ball.y,ball.x+50,ball.y+50,fill='black',width=0)
    circles.append(ball)
start = time.time()
main()
root.mainloop()
