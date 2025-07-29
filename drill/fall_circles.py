import tkinter
import random

class Circle:
    def __init__(self):
        self.size = random.randint(5,50)
        self.x = random.randint(0,500-self.size)
        self.y = random.randint(0,500-self.size)
        self.speedy = random.randint(1,5)

circles = []

def move():
    for en in circles:
        if en.y > 500:
            en.size = random.randint(5,50)
            en.x = random.randint(0,500-en.size)
            en.y = -en.size
            en.speedy = random.randint(1,5)
        en.y += en.speedy
        cvs.coords(en.id,en.x,en.y,
                   en.x+en.size,en.y+en.size)
    root.after(10, move)

root = tkinter.Tk()
root.title('円が落ちる')
cvs = tkinter.Canvas(root, width=500,
                    height=500,
                    bg='white')
cvs.pack()
for i in range(50):
    en = Circle()
    en.id = cvs.create_oval(en.x,en.y,
                en.x+en.size,en.y+en.size,
                fill='black',
                width=0)
    circles.append(en)

move()
root.mainloop()
