import tkinter
import random

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
    if player.y > 270:
        player.speedy = 0
        player.y = 270
    else:
        player.speedy += 0.3
    if key == 'Up' and player.speedy == 0:
        player.speedy = -12
    if key == 'Down':
        player.speedy += 2
    if key == 'Left':
        player.speedx -= 0.3
    if key == 'Right':
        player.speedx += 0.3
    player.speedx *= 0.98
    player.x += player.speedx
    player.y += player.speedy
    cvs.coords(player.id,player.x,player.y,player.x+30,player.y+30)

    for enemy in enemys:
        enemy.x -= 3
        if enemy.x < -enemy.size:
            enemy.x = random.randint(700,1400)
        hit(enemy)
        if enemy.atari:
            cvs.itemconfig(enemy.id,fill='red')
        cvs.coords(enemy.id,enemy.x,enemy.y,enemy.x+enemy.size,enemy.y+enemy.size)

    if hit_count == enemy_count:
        cvs.create_text(350,150,text='GAME OVER',fill='black',font=('Helvetica',30,'bold'))
        return

    root.after(10,move)

def hit(enemy):
    global hit_count
    x = ((player.x+15) - (enemy.x+enemy.size/2)) ** 2
    y = ((player.y+15) - (enemy.y+enemy.size/2)) ** 2
    dist = (x+y) ** 0.5
    pe = 15+enemy.size/2
    if dist < pe and not enemy.atari:
        enemy.atari = True
        hit_count += 1

root = tkinter.Tk()
root.title('ジャンプして避けろ')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
cvs = tkinter.Canvas(root, width=700, height=300, bg='white')
cvs.pack()
player = Circle()
player.x = 235
player.y = 235
player.speedx = 0
player.speedy = 0
player.id = cvs.create_oval(player.x,player.y,player.x+30,player.y+30,fill='black',width=0)

hit_count = 0
enemy_count = 5
enemys = []
for i in range(enemy_count):
    enemy = Circle()
    enemy.x = random.randint(700,1400)
    enemy.size = random.randint(20,150)
    enemy.y = 300-enemy.size
    enemy.id = cvs.create_oval(enemy.x,enemy.y,enemy.x+enemy.size,enemy.y+enemy.size,fill='blue',width=0)
    enemy.atari = False
    enemys.append(enemy)

move()
root.mainloop()