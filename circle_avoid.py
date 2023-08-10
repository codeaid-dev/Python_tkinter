import tkinter, random, time

class Circle:
    pass

def motion(e):
    cvs.coords(player.id,e.x-player.size/2,e.y-player.size/2,
               e.x+player.size/2,e.y+player.size/2)
    player.x = e.x-player.size/2
    player.y = e.y-player.size/2

start = False
stime = 0
def pressed(e):
    global start, stime
    if start:
        return
    cvs.delete('start')
    start = True
    stime = time.time()
    main()

enemies = []
def main():
    over = False
    for enemy in enemies:
        if enemy.y > 600:
            enemy.size = random.randint(5,50)
            enemy.x = random.randint(0,500-enemy.size)
            enemy.y = -enemy.size
            enemy.speedy = random.randint(1,6)
        enemy.y += enemy.speedy
        cvs.coords(enemy.id,enemy.x,enemy.y,
                   enemy.x+enemy.size,enemy.y+enemy.size)
        if collide(player,enemy):
            over = True
    if player.x < 0 or player.x > 400-player.size or player.y < 0 or player.y > 600-player.size:
        over = True
    if over:
        etime = time.time()-stime
        cvs.create_text(200,300,text='GAME OVER',fill='black',font=FONT)
        cvs.create_text(200,350,text=f'{etime:.0f} sec',fill='black',font=FONT)
        return

    root.after(10,main)

def collide(player, enemy):
    id1_x0,id1_y0,id1_x1,id1_y1 = cvs.coords(player.id)
    id2_x0,id2_y0,id2_x1,id2_y1 = cvs.coords(enemy.id)
    dist = (abs((id2_x0+enemy.size/2) - (id1_x0+player.size/2))**2 + abs((id2_y0+enemy.size/2) - (id1_y0+player.size/2))**2) ** 0.5
    if dist <= player.size/2+enemy.size/2:
        return True
    return False

root = tkinter.Tk()
root.title('落ちてくる円を避ける')
root.bind('<Motion>',motion)
root.bind('<Button>',pressed)
cvs = tkinter.Canvas(root, width=400,
                    height=600,
                    bg='white')
cvs.pack()
player = Circle()
player.size = 30
player.id = cvs.create_oval(0,0,0,0,fill='black',width=0)

for i in range(20):
    enemy = Circle()
    enemy.size = random.randint(5,50)
    enemy.x = random.randint(0,400-enemy.size)
    enemy.y = random.randint(0,600-enemy.size)
    enemy.speedy = random.randint(1,6)
    enemy.fill = 'red'
    enemy.id = cvs.create_oval(enemy.x,enemy.y,
                enemy.x+enemy.size,enemy.y+enemy.size,
                fill=enemy.fill,
                width=0)
    enemies.append(enemy)

FONT=('Times New Roman',30,'bold')
cvs.create_text(200,300,text='Mouse Press : Start',tags='start',fill='black',font=FONT)

root.mainloop()