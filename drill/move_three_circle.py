import tkinter
import random

class Circle:
    def __init__(self):
        self.x = random.randint(75,425)
        self.y = random.randint(75,425)
        self.dx = random.randint(1,5)
        self.dy = random.randint(1,5)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 75 or self.x > 425:
            self.dx *= -1
        if self.y < 25 or self.y > 475:
            self.dy *= -1
        for i,id in enumerate(self.id):
            cvs.coords(id,
                    self.x-75+i*50,self.y-25,
                    self.x-25+i*50,self.y+25)

    def draw(self):
        self.id = []
        for i in range(3):
            id = cvs.create_oval(self.x-75+i*50,self.y-25,
                                 self.x-25+i*50,self.y+25,
                                fill='black',
                                width=0)
            self.id.append(id)

def main():
    en.move()
    root.after(10, main)

root = tkinter.Tk()
root.title('3つ並んだ円を動かす')
cvs = tkinter.Canvas(root, width=500,
                    height=500,
                    bg='white')
cvs.pack()
en = Circle()
en.draw()
main()
root.mainloop()
