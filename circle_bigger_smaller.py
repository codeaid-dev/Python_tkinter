import tkinter

x1, y1, x2, y2 = 0, 0, 300, 300
m1, m2 = 1, -1

def move():
    global x1, x2, y1, y2, m1, m2
    x1 += m1
    y1 += m1
    x2 += m2
    y2 += m2
    if x1>150 or x1<0:
        m1 *= -1
    if x2>300 or x2<150:
        m2 *= -1
    cvs.coords(id,x1,y1,x2,y2)
    root.after(10, move)

root = tkinter.Tk()
root.title('円が大きくなったり小さくなったり')
cvs = tkinter.Canvas(root, width=300, height=300, bg='white')
cvs.pack()
id = cvs.create_oval(x1,y1,x2,y2,fill='black',width=0)

move()
root.mainloop()
