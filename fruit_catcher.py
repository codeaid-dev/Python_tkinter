import tkinter
import random

fx,fy = random.randint(0,470),-30
fs = random.randint(3,10)
px,py = 250,485
ps = 30
score = 0
timer = 0

def move(e):
    global px, py
    if e.keysym == 'Left':
        px -= ps
    if e.keysym == 'Right':
        px += ps

def main():
    global fx,fy,fs,score,timer
    timer += 1
    fy += fs
    if fy > 500:
        fx = random.randint(0,470)
        fy = -30
        fs = random.randint(3,10)
    cvs.coords('fruit',fx,fy,fx+30,fy+30)
    cvs.coords('player',px,py,px+50,py+10)
    if fx+30>=px and fx<=px+50 and fy+30>=py and fy<=py+10:
        score += 1
        fx = random.randint(0,470)
        fy = -30
        fs = random.randint(3,10)
    cvs.delete('score')
    cvs.create_text(250,250,text=f'score: {score}',font=('メイリオ',28),tag='score',fill='black')
    if timer >= 1000:
        return
    root.after(10,main)

root = tkinter.Tk()
root.title('フルーツキャッチャー')
root.bind('<Key>', move)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

cvs.create_rectangle(fx,fy,fx+30,fy+30,fill='red',width=0,tag='fruit')
cvs.create_rectangle(px,py,px+50,py+10,fill='black',width=0,tag='player')
main()
root.mainloop()