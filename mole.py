import tkinter
import random

moles = []
score = 0
timer = 0

class Mole:
    def __init__(self, x, y):
        w = random.randint(0,75)
        self.x1 = x + w
        self.y1 = y + w
        self.x2 = x+150 - w
        self.y2 = y+150 - w
        self.id = None
        self.dir = random.randint(2,5)
    def draw(self):
        self.id = cvs.create_oval(self.x1,self.y1,self.x2,self.y2,fill='brown',width=0)
    def change(self):
        self.x1 += self.dir
        self.y1 += self.dir
        self.x2 += (self.dir*-1)
        self.y2 += (self.dir*-1)
        if 75<=self.x1<=150 or 225<=self.x1<=300 or 375<=self.x1<=450 or self.x1<=0:
            self.dir *= -1
        cvs.delete(self.id)
        if 0<self.x1<10 or 150<self.x1<160 or 300<self.x1<310:
            self.id = cvs.create_oval(self.x1,self.y1,self.x2,self.y2,fill='orange',width=0)
        else:
            self.id = cvs.create_oval(self.x1,self.y1,self.x2,self.y2,fill='brown',width=0)

def click(e):
    global score
    x = e.x // 150
    y = e.y // 150
    index = x+y*3
    if 0<moles[index].x1<10 or 150<moles[index].x1<160 or 300<moles[index].x1<310:
        score += 1

def main():
    global timer
    timer += 1
    for m in moles:
        m.change()
    if timer > 200:
        cvs.create_text(225,225,text=f'GAME OVER ({score} hits)',fill='black',font=('メイリオ',32))
        return
    root.after(50,main)

root = tkinter.Tk()
root.title('ミニ・モグラたたき')
root.bind('<Button>', click)
cvs = tkinter.Canvas(root, width=450, height=450, bg='white')
cvs.pack()

for i in range(9):
    m = Mole(i%3*150,i//3*150)
    m.draw()
    moles.append(m)

main()
root.mainloop()