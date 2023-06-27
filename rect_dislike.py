import tkinter, random

def motion(e):
    global x,y
    if x < e.x < x+s and y < e.y < y+s:
        x = random.randint(0,500-s)
        y = random.randint(0,500-s)
        cvs.coords(id,x,y,x+s,y+s)

s = 50
x = random.randint(0,500-s)
y = random.randint(0,500-s)
root = tkinter.Tk()
root.title('嫌がる四角形')
root.bind('<Motion>',motion)
cvs = tkinter.Canvas(root, width=500,
                    height=500,
                    bg='white')
cvs.pack()
id = cvs.create_rectangle(x,y,x+s,y+s,fill='black',width=0)

root.mainloop()