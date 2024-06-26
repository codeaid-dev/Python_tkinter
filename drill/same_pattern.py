import tkinter
import random,time

class Rect():
    pass

def pressed(event):
    global over,clear,start,stime
    if not start:
        cvs.delete('start')
        start = True
        stime = time.time()
    if over or clear:
        return
    count = 0
    for i in range(25):
        if rights[i].x < event.x < rights[i].x+80 and rights[i].y < event.y < rights[i].y+80:
            if lefts[i].stat != rights[i].stat:
                if rights[i].stat == 'red':
                    rights[i].stat = 'white'
                    cvs.itemconfig(rights[i].id,fill='white')
                else:
                    rights[i].stat = 'red'
                    cvs.itemconfig(rights[i].id,fill='red')
            else:
                over = True
                cvs.create_text(410,200,text='GAME OVER',fill='black',font=('Helvetica',30,'bold'))
        if lefts[i].stat == rights[i].stat:
            count += 1
    if count == 25:
        clear = True
        etime = time.time()-stime
        cvs.create_text(410,200,text=f'GAME CLEAR',fill='blue',font=('Helvetica',30,'bold'))
        cvs.create_text(410,240,text=f'time: {etime:.0f}sec',fill='blue',font=('Helvetica',30,'bold'))

start = False
stime = 0
clear = False
over = False
lefts = []
rights = []

root = tkinter.Tk()
root.title('同じ模様')
root.bind('<Button>',pressed)
cvs = tkinter.Canvas(root, width=820, height=400, bg='white')
cvs.pack()
for i in range(25):
    left = Rect()
    left.x = i%5*80
    left.y = i//5*80
    left.stat = random.choice(['red','white'])
    left.id = cvs.create_rectangle(left.x,left.y,left.x+80,left.y+80,fill=left.stat,outline='black',width=2)
    lefts.append(left)

    right = Rect()
    right.x = 420+i%5*80
    right.y = i//5*80
    right.stat = random.choice(['red','white'])
    right.id = cvs.create_rectangle(right.x,right.y,right.x+80,right.y+80,fill=right.stat,outline='black',width=2)
    rights.append(right)

cvs.create_text(410,200,text='Click: Start',fill='black',font=('Helvetica',30,'bold'),tags='start')

root.mainloop()