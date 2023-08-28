import tkinter
import random

class Circle:
    def __init__(self):
        self.x = random.randint(0,450)
        self.y = random.randint(0,450)
        self.speedx = random.randint(1,3)
        self.speedy = random.randint(4,6)
        self.interval = random.randint(1,100)
        self.showing = True

circles = []

def pressed(event):
    for en in circles:
        dist = (abs(en.x+25-event.x)**2+abs(en.y+25-event.y)**2)**0.5
        if dist < 25 and en.showing:
            en.speedx,en.speedy = 0,0
            en.interval = 0
            en.showing = True

def move():
    for en in circles:
        if en.x > 450 or en.x < 0:
            en.speedx *= -1
        if en.y > 450 or en.y < 0:
            en.speedy *= -1
        en.x += en.speedx
        en.y += en.speedy
        cvs.coords(en.id,en.x,en.y,en.x+50,en.y+50)
        if en.interval != 0:
            en.interval += 1
        if en.interval!=0 and en.interval%100==0:
            en.showing = False if en.showing else True
        if en.showing:
            cvs.itemconfig(en.id,fill="black")
        else:
            cvs.itemconfig(en.id,fill="white")
    root.after(10, move)

root = tkinter.Tk()
root.title('動く円をクリック(点滅)')
root.bind('<Button>',pressed)
cvs = tkinter.Canvas(root, width=500,
                    height=500,
                    bg='white')
cvs.pack()
for i in range(4):
    en = Circle()
    en.id = cvs.create_oval(en.x,en.y,en.x+50,en.y+50,
                fill='black',
                width=0,
                tag='circle')
    circles.append(en)

move()
root.mainloop()
