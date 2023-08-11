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
        cvs.coords(enemy.id,enemy.x,enemy.y,enemy.x+enemy.size,enemy.y+enemy.size)

    root.after(10,move)

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

enemy_count = 5
enemys = []
for i in range(enemy_count):
    enemy = Circle()
    enemy.x = random.randint(700,1400)
    enemy.size = random.randint(20,150)
    enemy.y = 300-enemy.size
    enemy.id = cvs.create_oval(enemy.x,enemy.y,enemy.x+enemy.size,enemy.y+enemy.size,fill='blue',width=0)
    enemys.append(enemy)

move()
root.mainloop()