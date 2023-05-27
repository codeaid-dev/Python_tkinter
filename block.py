import tkinter
import random
import math

class Block:
    pass
Blocks = []
for y in range(6):
    for x in range(5):
        b = Block()
        b.x = x*100+60
        b.y = y*50+40
        Blocks.append(b)

key = ''
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ''

def colliderect(bar_x,bar_y,ball_x,ball_y,bar_width,bar_height):
    if ball_x>=bar_x and ball_x<=bar_x+bar_width:
        if ball_y+5>=bar_y and ball_y+5<=bar_y+bar_height or ball_y-5<=bar_y+bar_height and ball_y-5>=bar_y:
            return True
    return False

bar_x,bar_y = 275,780
ball_x,ball_y=300,400
speed=3
dir=-(random.randint(-45,45)+270)
over=False
clear=False
start=False
def main():
    global bar_x,bar_y,ball_x,ball_y,dir,over,clear,start
    if over:
        fnt=('Times New Roman',30,'bold')
        cvs.create_text(300,400,text='GAME OVER',fill='white',font=fnt)
        return
    if clear:
        fnt=('Times New Roman',30,'bold')
        cvs.create_text(300,400,text='GAME CLEAR',fill='white',font=fnt)
        return
    if key == 'Up':
        cvs.move('bar',0,-5)
        bar_y -= 5
    if key == 'Down':
        cvs.move('bar',0,5)
        bar_y += 5
    if key == 'Left':
        cvs.move('bar',-5,0)
        bar_x -= 5
    if key == 'Right':
        cvs.move('bar',5,0)
        bar_x += 5
    if key == 'space':
        start = True
    if start:
        cvs.coords(ball,ball_x-5,ball_y-5,ball_x+5,ball_y+5)
        ball_x+=math.cos(math.radians(dir))*speed
        ball_y+=math.sin(math.radians(dir))*speed
    if ball_x-5<0 or ball_x+5>600:
        dir = 180-dir
    if ball_y-5<0:
        dir *= -1
    if colliderect(bar_x,bar_y,ball_x,ball_y,50,10):
        dir = -(90 + (bar_x+25 - ball_x) / 50*80)
    if ball_y+5>800:
        over = True

    for block in Blocks:
        if block.id != None and colliderect(block.x,block.y,ball_x,ball_y,80,30):
            cvs.delete(block.id)
            block.id = None
            dir *= -1
            break
    for block in Blocks:
        if block.id != None:
            break
    else:
        clear = True

    root.after(10, main)

root = tkinter.Tk()
root.title('ブロック')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
root.geometry('600x800')
cvs = tkinter.Canvas(root, width=600, height=800, bg='black')
cvs.pack()
colors = ['#FF0000','#FF00FF','#FFFF00','#00FF00','#00FFFF','#0000FF']
for i,block in enumerate(Blocks):
    block.id = cvs.create_rectangle(block.x,block.y,block.x+80,block.y+30,fill=colors[int(i/5)],width=0,tags='block')
bar = cvs.create_rectangle(bar_x,bar_y,bar_x+50,bar_y+10,fill='white',tags='bar')
ball = cvs.create_oval(ball_x,ball_y,ball_x+10,ball_y+10,fill='white',tags='ball')
main()
root.mainloop()