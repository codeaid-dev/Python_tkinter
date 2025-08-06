import tkinter
import random

side = 125
stats = [0]*16 #0:黒い状態, 1:色表示, 2:揃っている
colors = ['red','green','blue','yellow','magenta','cyan','brown','orange']
tiles = []

def draw():
    cvs.delete('all')
    for i in range(16):
        x1 = i%4*side
        y1 = i//4*side
        x2 = i%4*side+side
        y2 = i//4*side+side
        if stats[i] == 0:
            cvs.create_rectangle(x1,y1,x2,y2,fill='black',outline='white')
        if stats[i] == 1:
            cvs.create_rectangle(x1,y1,x2,y2,fill=tiles[i],outline='white')

def shuffle():
    tiles.clear()
    while len(tiles) < 16:
        c = random.choice(colors)
        if tiles.count(c) < 2:
            tiles.append(c)

def click(e):
    x = e.x//side
    y = e.y//side
    i = x+y*4
    if 0<=i<=15:
        if stats[i] == 0:
            stats[i] = 1

def main():
    draw()
    root.after(200,main)

root = tkinter.Tk()
root.title('神経衰弱')
root.geometry('500x500')
root.bind('<Button>',click)

cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()

shuffle()
main()
root.mainloop()
