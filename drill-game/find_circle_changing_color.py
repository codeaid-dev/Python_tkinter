import tkinter, random, time

class Circle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.color = f'#{self.r:02X}{self.g:02X}{self.b:02X}'
        self.dr, self.dg, self.db = 1, 1, 1
        self.target = False

    def change_color(self):
        self.r += self.dr
        self.g += self.dg
        self.b += self.db
        self.color = f'#{self.r:02X}{self.g:02X}{self.b:02X}'
        if self.r == 0 or self.r == 255:
            self.dr *= -1
        if self.g == 0 or self.g == 255:
            self.dg *= -1
        if self.b == 0 or self.b == 255:
            self.db *= -1
        cvs.itemconfig(self.id, fill=self.color)

def pressed(e):
    global finish, spend
    for c in circles:
        diffX = e.x - (c.x+size/2)
        diffY = e.y - (c.y+size/2)
        dist = (diffX**2 + diffY**2)**0.5
        if dist < size/2 and not finish and c.target:
            spend = time.time() - start
            finish = True

circles = []
def main():
    for c in circles:
        if c.target:
            c.change_color()

    if finish:
        cvs.create_text(300,300,text=f'経過時間：{spend:.0f}秒',fill='black',font=('Helvetica', 30))
    root.after(300, main)

root = tkinter.Tk()
root.title('色が変化している円を見つけろ')
root.bind('<Button>', pressed)
cvs = tkinter.Canvas(root, width=600, height=600, bg='white')
cvs.pack()
start, spend = None, None
finish = False
size = 600/4
atari = random.randint(0,15)
# print(atari)
for i in range(16):
    x = i%4*size
    y = i//4*size
    c = Circle(x, y, size)
    c.id = cvs.create_oval(x, y,
                    x+size, y+size,
                    fill=c.color, width=0)
    if i == atari:
        c.target = True
    circles.append(c)

start = time.time()
main()
root.mainloop()
