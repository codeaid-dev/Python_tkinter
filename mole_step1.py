import tkinter
import random

moles = []

class Mole:
    def __init__(self, x, y):
        self.diameter = 150
        self.x = x
        self.y = y
        self.dir = 2
    def draw(self):
        self.id = cvs.create_oval(self.x,self.y,self.x+self.diameter,self.y+self.diameter,fill='brown',width=0)
    def change(self):
        self.x += self.dir
        self.y += self.dir
        self.diameter -= self.dir*2
        if 75<=self.x<=150 or 225<=self.x<=300 or 375<=self.x<=450 or self.x<=0:
            self.dir *= -1
        cvs.coords(self.id,self.x,self.y,self.x+self.diameter,self.y+self.diameter)

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