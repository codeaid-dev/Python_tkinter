import tkinter
import random

side = 125
one, two = None, None
count = 0
stat = 0
ids = []
colors = ['red','green','blue','yellow','magenta','cyan','purple','orange']
tiles = []
while len(tiles) < 16:
    c = random.choice(colors)
    if tiles.count(c) < 2:
        tiles.append(c)

def click(e):
    global stat, count
    for i in range(16):
        if i%4*side<e.x<i%4*side+side and i//4*side<e.y<i//4*side+side:
            cvs.itemconfig(ids[i], fill=tiles[i])
            if one == None:
                one = i
                break
            elif two == None:
                two = i
            elif one != None and two != None:
                if one != two:
                    cvs.itemconfig(ids[i], fill='black')


root = tkinter.Tk()
root.title('ミニ神経衰弱')
root.geometry('500x500')
root.bind('<Button>',click)

cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()

for i in range(16):
    id = cvs.create_rectangle(i%4*side,i//4*side,i%4*side+side,i//4*side+side,fill='black',outline='white')
    ids.append(id)

root.mainloop()