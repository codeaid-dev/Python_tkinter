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
        if en.x > 500-en.r or en.x < en.r:
            en.angle = 180 - en.angle
            en.fill =random.choice(colors)
            cvs.itemconfig(en.id,fill=en.fill)
        if en.y > 500-en.r or en.y < en.r:
            en.angle *= -1
            en.fill =random.choice(colors)
            cvs.itemconfig(en.id,fill=en.fill)
        en.x += en.speed*math.cos(math.radians(en.angle))
        en.y += en.speed*math.sin(math.radians(en.angle))
        cvs.coords(en.id,en.x-en.r,en.y-en.r,en.x+en.r,en.y+en.r)

    root.after(10, move)

def control(e):
    for en in circles:
        if en.stop:
            continue
        if collision(en, e.x, e.y):
            en.stop = True

def collision(en, x, y):
    id_x0,id_y0,id_x1,id_y1 = cvs.coords(en.id)
    dist = ((x-(id_x0+en.r))**2 + (y-(id_y0+en.r))**2) ** 0.5
    if dist <= en.r:
        return True
    return False

root = tkinter.Tk()
root.title('点と円の当たり判定')
root.bind('<ButtonPress>', control)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
for i in range(5):
    en = Circle()
    en.id = cvs.create_oval(en.x-en.r,en.y-en.r,
                            en.x+en.r,en.y+en.r,
                            fill=en.fill,width=0)
    circles.append(en)

move()

root.mainloop()