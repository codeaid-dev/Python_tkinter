import tkinter,math,random

dir=random.randint(0,360)
x,y=250,250
speed=5
dx = speed * math.cos(math.radians(dir))
dy = speed * math.sin(math.radians(dir))
def main():
    global x,y,dx,dy
    cvs.delete('circle')
    cvs.create_rectangle(0,0,
                         root.winfo_width(),
                         root.winfo_height(),
                         fill='white',width=0)
    x += dx
    y += dy
    cvs.create_oval(x-15,y-15,x+15,y+15,
                    fill='black',width=0,
                    tags='circle')
    if x < 15 or x > 485:
        dx *= -1
    if y < 15 or y > 485:
        dy *= -1
    root.after(17,main)

def update(e):
    global x,y,dx,dy
    x = e.x
    y = e.y
    dir=random.randint(0,360)
    dx = speed * math.cos(math.radians(dir))
    dy = speed * math.sin(math.radians(dir))

root = tkinter.Tk()
root.title('円がウロウロする(dx,dy)')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()
root.bind('<Button>', update)

main()
root.mainloop()