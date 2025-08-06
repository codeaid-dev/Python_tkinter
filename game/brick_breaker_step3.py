import tkinter,random

class Brick:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dx = random.randint(-3,3)
        self.dy = random.randint(2,4)
        self.r = 5
    def collide(self,obj):
        if self.x < obj.x:
            closestX = obj.x
        elif self.x > obj.x + obj.w:
            closestX = obj.x + obj.w
        else:
            closestX = self.x
        
        if self.y < obj.y:
            closestY = obj.y
        elif self.y > obj.y + obj.h:
            closestY = obj.y + obj.h
        else:
            closestY = self.y
        
        dx = self.x - closestX
        dy = self.y - closestY
        distance = (dx**2 + dy**2)**0.5
        return distance < self.r

keys = set()
def key_down(e):
    keys.add(e.keysym)
def key_up(e):
    keys.discard(e.keysym)

bricks = []
for y in range(6):
    for x in range(5):
        b = Brick(x*100+60,y*50+40,80,30)
        bricks.append(b)

over=False
clear=False
start=False
def main():
    global start,over,clear
    if over:
        fnt=('Times New Roman',30,'bold')
        cvs.create_text(300,400,text='GAME OVER',fill='white',font=fnt)
        return
    if clear:
        fnt=('Times New Roman',30,'bold')
        cvs.create_text(300,400,text='GAME CLEAR',fill='white',font=fnt)
        return
    if 'Left' in keys:
        cvs.move(bar.id,-5,0)
        bar.x -= 5
    if 'Right' in keys:
        cvs.move(bar.id,5,0)
        bar.x += 5
    if 'space' in keys:
        start = True
    if start:
        cvs.coords(ball.id,ball.x-ball.r,ball.y-ball.r,
                   ball.x+ball.r,ball.y+ball.r)
        ball.x += ball.dx
        ball.y += ball.dy
    if ball.x<ball.r or ball.x>600-ball.r:
        ball.dx *= -1
    if ball.y<ball.r:
        ball.dy *= -1
    if ball.y>800-ball.r:
        over = True
    if ball.collide(bar):
        ball.dy = -abs(ball.dy)

    for b in bricks:
        if b.id != None and ball.collide(b):
            cvs.delete(b.id)
            b.id = None
            ball.dy *= -1
            break
    for b in bricks:
        if b.id != None:
            break
    else:
        clear = True

    root.after(10, main)

root = tkinter.Tk()
root.title('ブロック崩し')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
root.geometry('600x800')
cvs = tkinter.Canvas(root,width=600,height=800,bg='black')
cvs.pack()

colors = ['#FF0000','#FF00FF','#FFFF00','#00FF00','#00FFFF','#0000FF']
for i,b in enumerate(bricks):
    b.id = cvs.create_rectangle(b.x,b.y,
                                b.x+b.w,b.y+b.h,
                                fill=colors[int(i/5)],
                                width=0,tags='brick')

bar = Brick(275,780,50,10)
bar.id = cvs.create_rectangle(bar.x,bar.y,
                              bar.x+bar.w,bar.y+bar.h,
                              fill='white',tags='bar')
ball = Ball(295,395)
ball.id = cvs.create_oval(ball.x-ball.r,ball.y-ball.r,
                          ball.x+ball.r,ball.y+ball.r,
                          fill='white',tags='ball')
main()
root.mainloop()