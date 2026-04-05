import tkinter
import random, math

class Circle:
    def __init__(self):
        self.x = random.randint(25,475)
        self.y = random.randint(25,475)
        self.speed = 5
        self.r = 25
        self.angle = random.randint(0,360)
        self.fill = 'black'
        self.stop = False

circles = []
colors = ['red','green','blue']
def move():
    for en in circles:
        if en.stop:
            continue
        if en.x > 475 or en.x < 25:
            en.angle = 180 - en.angle
            en.fill =random.choice(colors)
            cvs.itemconfig(en.id,fill=en.fill)
        if en.y > 475 or en.y < 25:
            en.angle *= -1
            en.fill =random.choice(colors)
            cvs.itemconfig(en.id,fill=en.fill)
        en.x += en.speed*math.cos(math.radians(en.angle))
        en.y += en.speed*math.sin(math.radians(en.angle))
        cvs.coords(en.id,en.x-25,en.y-25,en.x+25,en.y+25)

    root.after(10, move)

def control(e):
    for en in circles:
        if en.stop:
            continue
        if collide(en.id, e.x, e.y):
            en.stop = True

def collide(id, x, y):
    id_x0,id_y0,id_x1,id_y1 = cvs.coords(id)
    dist = ((x-(id_x0+25))**2 + (y-(id_y0+25))**2) ** 0.5
    if dist <= 25:
        return True
    return False

root = tkinter.Tk()
root.title('点と円の当たり判定')
root.bind('<ButtonPress>', control)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
for i in range(5):
    en = Circle()
    en.id = cvs.create_oval(en.x-25,en.y-25,
                            en.x+25,en.y+25,
                            fill=en.fill,width=0)
    circles.append(en)

move()

root.mainloop()