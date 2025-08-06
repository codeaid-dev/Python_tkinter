import tkinter
import random

class Circle: # step3
    def collide(self,obj):
        x = ((self.x+self.size/2) - (obj.x+obj.size/2)) ** 2
        y = ((self.y+self.size/2) - (obj.y+obj.size/2)) ** 2
        dist = (x+y) ** 0.5
        pe = self.size/2+obj.size/2
        if dist < pe and not obj.atari:
            obj.atari = True
            return True
        else:
            return False

player = None
key = ''
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ''

def move():
    global hit_count # step3
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
    cvs.coords(player.id,player.x,player.y,player.x+player.size,player.y+player.size)

    for enemy in enemies:
        enemy.x -= 3
        if enemy.x < -enemy.size:
            enemy.x = random.randint(700+enemy.size,1400-enemy.size)
        # step3 -->
        if player.collide(enemy):
            hit_count += 1
        if enemy.atari:
            cvs.itemconfig(enemy.id,fill='red')
        # <-- step3
        cvs.coords(enemy.id,enemy.x,enemy.y,enemy.x+enemy.size,enemy.y+enemy.size)
    # step3 -->
    if hit_count == enemy_count:
        cvs.create_text(350,150,text='GAME OVER',fill='black',font=('Helvetica',30,'bold'))
        return
    # <-- step3
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
player.size = 30
player.id = cvs.create_oval(player.x,player.y,player.x+player.size,player.y+player.size,fill='black',width=0)

hit_count = 0 # step3
enemy_count = 5
enemies = []
for i in range(enemy_count):
    enemy = Circle()
    enemy.size = random.randint(20,150)
    enemy.x = random.randint(700+enemy.size,1400-enemy.size)
    enemy.y = 300-enemy.size
    enemy.id = cvs.create_oval(enemy.x,enemy.y,enemy.x+enemy.size,enemy.y+enemy.size,fill='blue',width=0)
    enemy.atari = False # step3
    enemies.append(enemy)

move()
root.mainloop()