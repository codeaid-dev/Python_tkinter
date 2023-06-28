import tkinter, random

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
    root.after(10,move)

root = tkinter.Tk()
root.title('円をスムーズに動かす')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
player = Circle()
player.x = 35
player.y = 35
player.speedx = 0
player.speedy = 0
player.id = cvs.create_oval(player.x,player.y,player.x+30,player.y+30,fill='black',width=0)

move()
root.mainloop()