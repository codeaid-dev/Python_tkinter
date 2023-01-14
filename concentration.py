import tkinter
import random

side = 125
one, two = None, None
timer = 0
proc = 0
stats = [0]*16
colors = ['red','green','blue','yellow','magenta','cyan','purple','orange']
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
        if stats[i] == 1 or stats[i] == 2:
            cvs.create_rectangle(x1,y1,x2,y2,fill=tiles[i],outline='white')

def suffle():
    tiles.clear()
    while len(tiles) < 16:
        c = random.choice(colors)
        if tiles.count(c) < 2:
            tiles.append(c)

def click(e):
    global proc, timer, one, two
    x = e.x//side
    y = e.y//side
    i = x+y*4
    if 0<=i<=15:
        if stats[i] == 0:
            if proc == 1:
                stats[i] = 1
                one = i
                proc = 2
            elif proc == 2:
                stats[i] = 1
                two = i
                proc = 3
                timer = 0

def main():
    global proc, timer
    timer += 1
    draw()
    if proc == 0:
        suffle()
        proc = 1
#    if proc == 1:
#        print('1枚目')
#    if proc == 2:
#        print('2枚目')
    if proc == 3 and timer == 5:
        if tiles[one] == tiles[two]:
            stats[one] = 2
            stats[two] = 2
        else:
            stats[one] = 0
            stats[two] = 0
        proc = 1
    root.after(200,main)

root = tkinter.Tk()
root.title('ミニ神経衰弱')
root.geometry('500x500')
root.bind('<Button>',click)

cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()

main()
root.mainloop()