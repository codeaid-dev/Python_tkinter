import tkinter,random

class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dx = random.randint(1,5)
        self.dy = random.randint(1,5)
        self.move = False
        self.radius = 0

def press(e):
    en = Circle(e.x, e.y)
    en.id = cvs.create_oval(en.x,en.y,en.x,en.y,fill='yellow',width=0)
    circles.append(en)

def release(e):
    for en in circles:
        if not en.move:
            en.move = True

def drag(e):
    for en in circles:
        if not en.move:
            dst = ((e.x-en.x)**2 + (e.y-en.y)**2) ** 0.5
            cvs.coords(en.id,en.x-dst,en.y-dst,en.x+dst,en.y+dst)
            en.radius = dst

def main():
    for en in circles:
        if en.move:
            en.x += en.dx
            en.y += en.dy
            if en.x < en.radius or en.x > 500-en.radius:
                en.dx *= -1
            elif en.y < en.radius or en.y > 500-en.radius:
                en.dy *= -1
            cvs.coords(en.id,en.x-en.radius,en.y-en.radius,
                       en.x+en.radius,en.y+en.radius)

    root.after(10,main)

circles = []
root = tkinter.Tk()
root.title('ドラッグで描いた円が移動する')
root.geometry('500x500')
root.bind('<Button1-Motion>',drag)
root.bind('<ButtonPress>',press)
root.bind('<ButtonRelease>',release)
cvs = tkinter.Canvas(root,width=500,height=500,bg='black')
cvs.pack()
main()
root.mainloop()
