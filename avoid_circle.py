import tkinter
import random

x, y = [75,225,325], [225,225,225]
speedx, speedy = [3,2,3], [2,3,1]
id = [0]*3
fills = ['black']*3
colors = ['red','green','blue']
player = 0
def move():
    cvs.delete('circle')
    over = False
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
        id[i] = cvs.create_oval(x[i],y[i],x[i]+50,y[i]+50,fill=fills[i],width=0,tags='circle')
        if player != 0 and collide(id[i], player):
            over = True
    if over:
        return

    root.after(10, move)

def control(e):
    global player
    cvs.delete('player')
    player = cvs.create_oval(e.x-50,e.y-50,
                    e.x+50,e.y+50,
                    fill='gray',
                    width=0,
                    tags='player')

def collide(id1, id2):
    id1_x0,id1_y0,id1_x1,id1_y1 = cvs.coords(id1)
    id2_x0,id2_y0,id2_x1,id2_y1 = cvs.coords(id2)
    dist = (abs((id2_x0+50) - (id1_x0+25))**2 + abs((id2_y0+50) - (id1_y0+25))**2) ** 0.5
    if dist <= 75:
        return True
    return False

root = tkinter.Tk()
root.title('円が当たったら止まる')
root.bind('<Motion>', control)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

move()

root.mainloop()