import tkinter
import random

class Sprite:
    def __init__(self,x=0,y=0,s=0):
        self.x = x
        self.y = y
        self.s = s
        self.id = None
    def is_hit(self,sprite):
        subx = abs(sprite.x-self.x)
        suby = abs(sprite.y-self.y)
        dist = (subx**2 + suby**2) ** 0.5
        return dist <= self.s/2 + sprite.s/2

enemys = []
bullets = []
count = 0
over = False
over_msg = 0
score = 0
score_msg = 0

key = ''
def key_down(e):
    global key
    key = e.keysym
    if key == 'space':
        bullets.append(Sprite())
def key_up(e):
    global key
    key = ''

def move():
    if key == 'Up':
        canvas.move('fighter',0,-5)
        canvas.move(player.id,0,-5)
        player.y -= 5
    if key == 'Down':
        canvas.move('fighter',0,5)
        canvas.move(player.id,0,5)
        player.y += 5
    if key == 'Left':
        canvas.move('fighter',-5,0)
        canvas.move(player.id,-5,0)
        player.x -= 5
    if key == 'Right':
        canvas.move('fighter',5,0)
        canvas.move(player.id,5,0)
        player.x += 5
    root.after(10,move)

def main():
    global count,over,score, over_msg, score_msg
    if over:
        fnt=('Times New Roman',30,'bold')
        over_msg = canvas.create_text(250,400,text='GAME OVER',fill='white',font=fnt)
        score_msg = canvas.create_text(250,450,text=score,fill='white',font=fnt)
        return
    for bullet in bullets:
        bullet.y -= 10
        if bullet.id != None:
            if bullet.y < 0:
                bullets.remove(bullet)
                canvas.delete(bullet.id)
            else:
                canvas.coords(bullet.id,bullet.x-5,bullet.y,bullet.x+5,bullet.y+10)
        else:
            bullet.x = canvas.coords('fighter')[0]
            bullet.y = canvas.coords('fighter')[1]-32
            bullet.id = canvas.create_oval(bullet.x-5,bullet.y,bullet.x+5,bullet.y+10,fill='red',width=0)
        for e in enemys:
            if e.is_hit(bullet):
                score += int(1000/e.s)
                bullets.remove(bullet)
                canvas.delete(bullet.id)
                enemys.remove(e)
                canvas.delete(e.id)

    count += 1
    if count % 10 == 0:
        enemys.append(Sprite(random.randint(0,500),0,random.randint(10,50)))

    for e in enemys:
        e.y += 5
        if e.id != None:
            if e.y > 800:
                enemys.remove(e)
                canvas.delete(e.id)
            else:
                canvas.coords(e.id, e.x-e.s/2, e.y-e.s/2, e.x+e.s/2, e.y+e.s/2)
        else:
            e.id = canvas.create_oval(e.x-e.s/2, e.y-e.s/2, e.x+e.s/2, e.y+e.s/2,fill='gray',width=0,tags='enemy')
        if e.is_hit(player):
            over = True
    root.after(10,main)

def reset():
    global count, over, score, over_msg, score_msg
    over = False
    score = 0
    canvas.delete(score_msg)
    canvas.delete(over_msg)
    for e in enemys:
        enemys.remove(e)
    canvas.delete('enemy')
    main()

root = tkinter.Tk()
root.title('サークルシューティング')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
canvas = tkinter.Canvas(root, width=500, height=800, bg='black')
canvas.pack()
fighter = tkinter.PhotoImage(file='images/fighter_white.png')
fighter = fighter.subsample(4)
canvas.update()
posx,posy = canvas.winfo_width()/2,canvas.winfo_height()/4*3
canvas.create_image(posx,posy,image=fighter,tags='fighter')
player = Sprite(posx,posy,40)
player.id = canvas.create_oval(posx-20,posy-20,posx+20,posy+20,width=0)

my_menu = tkinter.Menu(root)
root.config(menu=my_menu)
options_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='オプション', menu=options_menu)
options_menu.add_command(label='リセット', command=reset)

main()
move()
root.mainloop()