import tkinter,random,math

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
        self.dir = random.randint(45,135)
        self.speed=3
    def collide(self,obj):
        if self.x+10>obj.x and self.x<obj.x+obj.w:
            if self.y+10>obj.y and self.y<obj.y+obj.h:
                return True
        return False

key = ''
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ''

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
    if key == 'Left':
        cvs.move(bar.id,-5,0)
        bar.x -= 5
    if key == 'Right':
        cvs.move(bar.id,5,0)
        bar.x += 5
    if key == 'space':
        start = True
    if start:
        cvs.coords(ball.id,ball.x,ball.y,
                   ball.x+10,ball.y+10)
        ball.x+=math.cos(math.radians(ball.dir))*ball.speed
        ball.y+=math.sin(math.radians(ball.dir))*ball.speed
    if ball.x<0 or ball.x>590:
        ball.dir = 180 - ball.dir
    if ball.y<0:
        ball.dir *= -1
    if ball.y>790:
        over = True
    if ball.collide(bar):
        position = (bar.x+bar.w - ball.x) / bar.w #バーの当たった位置(0~1)
        ball.dir = -(position*100+40) #反射後の角度(40~140)

    for b in bricks:
        if b.id != None and ball.collide(b):
            cvs.delete(b.id)
            b.id = None
            ball.dir *= -1
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
ball.id = cvs.create_oval(ball.x,ball.y,
                          ball.x+10,ball.y+10,
                          fill='white',tags='ball')
main()
root.mainloop()