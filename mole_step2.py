import tkinter
import random

moles = []

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
        self.id = cvs.create_oval(self.x1,self.y1,self.x2,self.y2,fill='brown',width=0)

def main():
    for m in moles:
        m.change()
    root.after(50,main)

root = tkinter.Tk()
root.title('ミニ・モグラたたき')
cvs = tkinter.Canvas(root, width=450, height=450, bg='white')
cvs.pack()

for i in range(9):
    m = Mole(i%3*150,i//3*150)
    m.draw()
    moles.append(m)

main()
root.mainloop()