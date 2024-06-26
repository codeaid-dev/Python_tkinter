import tkinter
import random

x, y = [75,225,325], [225,225,225]
speedx, speedy = [3,2,3], [2,3,1]
id = [0]*3
fills = ['black']*3
colors = ['red','green','blue']
def move():
    for i in range(3):
        if x[i] > 450 or x[i] < 0:
            speedx[i] *= -1
            fills[i] =random.choice(colors)
            cvs.itemconfig(id[i],fill=fills[i])
        if y[i] > 450 or y[i] < 0:
            speedy[i] *= -1
            fills[i] =random.choice(colors)
            cvs.itemconfig(id[i],fill=fills[i])
        x[i] += speedx[i]
        y[i] += speedy[i]
        cvs.coords(id[i],x[i],y[i],x[i]+50,y[i]+50)
    root.after(10, move)

root = tkinter.Tk()
root.title('円の色を変える')
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
for i in range(3):
    id[i] = cvs.create_oval(x[i],y[i],x[i]+50,y[i]+50,fill='black',width=0,tag='circle')

move()
root.mainloop()