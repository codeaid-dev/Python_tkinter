import tkinter, time, random

class Circle:
    pass

player = None
key = ''
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ''

def move():
    if key == 'Up':
        player.speedy -= 0.1
    if key == 'Down':
        player.speedy += 0.1
    if key == 'Left':
        player.speedx -= 0.1
    if key == 'Right':
        player.speedx += 0.1
    player.speedx *= 0.98
    player.speedy *= 0.98
    player.x += player.speedx
    player.y += player.speedy
    cvs.coords(player.id,player.x,player.y,player.x+30,player.y+30)
    for wall in walls:
      if collide(player, wall) and wall.num == goal:
          etime = time.time()-stime
          cvs.create_text(250,250,text='CLEAR',fill='black',font=('Helvetica',30))
          cvs.create_text(250,280,text=f'{etime:.0f} sec',fill='black',font=('Helvetica',30))
          return
      if collide(player, wall) or player.x<0 or player.x>470 or player.y<0 or player.y>470:
          cvs.create_text(250,250,text='GAME OVER',fill='black',font=('Helvetica',30))
          return
    root.after(10,move)

def collide(player, wall):
    id1_x0,id1_y0,id1_x1,id1_y1 = cvs.coords(player.id)
    id2_x0,id2_y0,id2_x1,id2_y1 = cvs.coords(wall.id)
    dist = (abs((id2_x0+52/2) - (id1_x0+30/2))**2 + abs((id2_y0+52/2) - (id1_y0+30/2))**2) ** 0.5
    if dist <= 30/2+52/2:
        return True
    return False

root = tkinter.Tk()
root.title('通路を抜けろ')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
player = Circle()
player.x = 5
player.y = 5
player.speedx = 0
player.speedy = 0
player.id = cvs.create_oval(player.x,player.y,player.x+30,player.y+30,fill='black',width=0)

walls = []
num = 1
goal = random.randint(1,25)
for y in range(5):
    for x in range(5):
        wall = Circle()
        wall.x = x*(52+40)+40
        wall.y = y*(52+40)+40
        wall.id = cvs.create_oval(wall.x,wall.y,wall.x+52,wall.y+52,fill='red',width=0)
        wall.num = num
        if num == goal:
            cvs.itemconfig(wall.id,fill='blue')
        num += 1
        walls.append(wall)
stime = time.time()
move()
root.mainloop()