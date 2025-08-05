import tkinter, random

class Circle:
    def __init__(self):
        self.size = random.randint(20,30)
        self.x = random.randint(0,500-self.size)
        self.y = random.randint(0,500-self.size)
        self.dx = random.randint(1,5)
        self.dy = random.randint(1,5)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color = f'#{r:02X}{g:02X}{b:02X}'

    def move(self):
        if self.x > 500-self.size or self.x < 0:
            self.dx *= -1
        if self.y > 500-self.size or self.y < 0:
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy
        cvs.coords(self.id, self.x, self.y,
                   self.x+self.size, self.y+self.size)

    def draw(self):
        self.id = cvs.create_oval(self.x, self.y,
                        self.x+self.size, self.y+self.size,
                        fill=self.color,
                        width=0)

circles = []

def main():
    for c in circles:
        c.move()

    root.after(16, main)

root = tkinter.Tk()
root.title('複数の円がウロウロ動く')
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
for i in range(50):
    c = Circle()
    c.draw()
    circles.append(c)
main()
root.mainloop()
