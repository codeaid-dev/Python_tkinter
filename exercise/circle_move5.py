import tkinter
import random

class Circle:
    def __init__(self):
        self.x = random.randint(0,450)
        self.y = random.randint(0,450)
        self.speedx = random.randint(2,3)
        self.speedy = random.randint(1,3)
        self.fill = 'black'

circles = []
colors = ['red','green','blue']
def move():
    for en in circles:
        if en.x > 450 or en.x < 0:
            en.speedx *= -1
            en.fill =random.choice(colors)
            cvs.itemconfig(en.id,fill=en.fill)
        if en.y > 450 or en.y < 0:
            en.speedy *= -1
            en.fill =random.choice(colors)
            cvs.itemconfig(en.id,fill=en.fill)
        en.x += en.speedx
        en.y += en.speedy
        cvs.coords(en.id,en.x,en.y,en.x+50,en.y+50)
    root.after(10, move)

root = tkinter.Tk()
root.title('円のオブジェクト化')
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
for i in range(3):
    en = Circle()
    en.id = cvs.create_oval(en.x,en.y,
                            en.x+50,en.y+50,
                            fill=en.fill,width=0)
    circles.append(en)

move()
root.mainloop()