import tkinter
import random

moles = []
score = 0
timer = 0

class Mole:
    def __init__(self, x, y):
        self.diameter = random.randint(0,150)
        self.x = x+((150-self.diameter)/2)
        self.y = y+((150-self.diameter)/2)
        self.dir = random.randint(2,5)
    def draw(self):
        self.id = cvs.create_oval(self.x,self.y,self.x+self.diameter,self.y+self.diameter,fill='brown',width=0)
    def change(self):
        self.x += self.dir
        self.y += self.dir
        self.diameter -= self.dir*2
        if 75<=self.x<=150 or 225<=self.x<=300 or 375<=self.x<=450 or self.x<=0:
            self.dir *= -1
        cvs.coords(self.id,self.x,self.y,self.x+self.diameter,self.y+self.diameter)
        if 0<self.x<10 or 150<self.x<160 or 300<self.x<310:
            cvs.itemconfig(self.id,fill='orange')
        else:
            cvs.itemconfig(self.id,fill='brown')

def click(e):
    global score
    x = e.x // 150
    y = e.y // 150
    index = x+y*3
    if 0<moles[index].x<10 or 150<moles[index].x<160 or 300<moles[index].x<310:
        score += 1

def main():
    global timer
    timer += 1
    for m in moles:
        m.change()
    if timer > 200:
        cvs.create_text(225,225,text=f'GAME OVER ({score} hits)',fill='black',font=('Helvetica',32))
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