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
player = 0
def move():
    over = False
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
        if player != 0 and collide(en.id, player):
            over = True
    if over:
        return

    root.after(10, move)

def control(e):
    cvs.coords(player,e.x-50,e.y-50,e.x+50,e.y+50)

def collide(id1, id2):
    id1_x0,id1_y0,id1_x1,id1_y1 = cvs.coords(id1)
    id2_x0,id2_y0,id2_x1,id2_y1 = cvs.coords(id2)
    dist = (((id2_x0+50)-(id1_x0+25))**2 + ((id2_y0+50)-(id1_y0+25))**2) ** 0.5
    if dist <= 75:
        return True
    return False

root = tkinter.Tk()
root.title('円が当たったら止まる')
root.bind('<Motion>', control)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
for i in range(3):
    en = Circle()
    en.id = cvs.create_oval(en.x,en.y,
                            en.x+50,en.y+50,
                            fill=en.fill,width=0)
    circles.append(en)

player = cvs.create_oval(-100,-100,
                    0,0,
                    fill='gray',
                    width=0,
                    tag='player')
move()

root.mainloop()