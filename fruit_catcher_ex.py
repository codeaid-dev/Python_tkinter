import tkinter
import random

fx,fy = random.randint(25,475),-25
fs = random.randint(3,10)
px,py = 250,491
ps = 0
score = 0
timer = 0

key = ''
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ''

def move():
    global ps,px
    if key == 'Left':
        ps -= 1
    if key == 'Right':
        ps += 1
    ps *= 0.98
    px += ps
    cvs.coords(kago,px,py)
    root.after(10,move)

def main():
    global fx,fy,fs,score,timer
    timer += 1
    fy += fs
    if fy > 525:
        fx = random.randint(25,475)
        fy = -25
        fs = random.randint(3,10)
    cvs.coords(fruit,fx,fy)
    if fx+25>=px-25 and fx-25<=px+25 and fy+25>=py-9 and fy-25<=py+9:
        score += 1
        fx = random.randint(25,475)
        fy = -25
        fs = random.randint(3,10)
    cvs.delete('score')
    cvs.create_text(250,250,text=f'score: {score}',font=('メイリオ',28),tag='score',fill='black')
    if timer >= 3000:
        return
    root.after(10,main)

root = tkinter.Tk()
root.title('フルーツキャッチャー')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

fruit_img = tkinter.PhotoImage(file='images/fruit_ringo_50.png')
fruit = cvs.create_image(fx,fy,image=fruit_img)
kago_img = tkinter.PhotoImage(file='images/fruit_kago_50.png')
kago = cvs.create_image(px,py,image=kago_img)
move()
main()
root.mainloop()