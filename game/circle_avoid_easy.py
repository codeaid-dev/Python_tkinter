import tkinter, random, time

class Circle:
    pass

def motion(e):
    player.x = e.x
    player.y = e.y
    cvs.coords(player.id,e.x-25,e.y-25,e.x+25,e.y+25)

def move():
    global over
    for en in ens:
        en.x += en.dx
        en.y += en.dy
        if en.x < 25 or en.x > 475:
            en.dx *= -1
        if en.y < 25 or en.y > 475:
            en.dy *= -1
        cvs.coords(en.id,en.x-25,en.y-25,en.x+25,en.y+25)
        over = False
        if ((player.x-en.x)**2 + (player.y-en.y)**2)**0.5 < 50:
            over = True
        if player.x < 25 or player.x > 475 or player.y < 25 or player.y > 475:
            over = True
        if over:
            etime = time.time()-stime
            cvs.create_text(250,250,text=f'GAME OVER : {etime:.0f}sec\nrestart : press R',
                            tags='start',fill='black',
                            font=('helvetica',30,'bold'))
            return

    root.after(10,move)

start = False
stime = 0
def pressed(e):
    global start, stime
    if start:
        return
    cvs.delete('start')
    start = True
    stime = time.time()
    move()

def key(e):
    if e.keysym.upper() == 'R':
        if over:
            reset()

def reset():
    global start
    start = False
    cvs.delete('start')
    cvs.create_text(250,250,text='Mouse Press : Start',
                    tags='start',fill='black',
                    font=('helvetica',30,'bold'))

root = tkinter.Tk()
root.title('円を避けるゲーム')
root.bind('<Motion>', motion)
root.bind('<Button>', pressed)
root.bind('<Key>', key)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
player = Circle()
player.id = cvs.create_oval(0,0,
                    0,0,
                    fill='black',
                    width=0)

ens = []
for i in range(10):
    en = Circle()
    en.x = random.randint(25,475)
    en.y = random.randint(25,475)
    en.dx = random.randint(2,3)
    en.dy = random.randint(1,3)
    en.id = cvs.create_oval(en.x-25,en.y-25,en.x+25,en.y+25,fill='red',width=0)
    ens.append(en)

reset()

root.mainloop()