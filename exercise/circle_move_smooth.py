import tkinter

class Circle:
    pass

player = None
keys = set()
def key_down(e):
    keys.add(e.keysym)
def key_up(e):
    keys.discard(e.keysym)

def move():
    if 'Up' in keys:
        player.speedy -= 0.1
    if 'Down' in keys:
        player.speedy += 0.1
    if 'Left' in keys:
        player.speedx -= 0.1
    if 'Right' in keys:
        player.speedx += 0.1
    player.speedx *= 0.98
    player.speedy *= 0.98
    player.x += player.speedx
    player.y += player.speedy
    cvs.coords(player.id,player.x,player.y,player.x+30,player.y+30)
    root.after(16,move) # 約60fps（1000ms / 60 ≒ 16）

root = tkinter.Tk()
root.title('円をスムーズに動かす')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
player = Circle()
player.x = 235
player.y = 235
player.speedx = 0
player.speedy = 0
player.id = cvs.create_oval(player.x,player.y,player.x+30,player.y+30,fill='black',width=0)
#player.id = cvs.create_oval(player.x,player.y,player.x+30,player.y+30,fill='#ff00ff',width=0)

move()
root.mainloop()