import tkinter, random, time

class Tile:
    def __init__(self,x,y,side):
        self.x = x
        self.y = y
        self.side = side
        self.color = 'white' if random.randint(0,1) == 0 else 'black'
        self.id = None
    def change(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'
        cvs.itemconfig(self.id,fill=self.color)
    def is_hit(self,mx,my):
        return self.x < mx < self.x+self.side and \
                self.y < my < self.y+self.side
    def draw(self):
        self.id = cvs.create_rectangle(self.x,self.y,
                                    self.x+self.side,
                                    self.y+self.side,
                                    fill=self.color,
                                    outline='gray',
                                    width=2)
tiles = []
for i in range(9):
    t = Tile(i%3*150,i//3*150,150)
    tiles.append(t)

def pressed(event):
    if finished:
        return
    for index, tile in enumerate(tiles):
        if tile.is_hit(event.x,event.y):
            tiles[index].change()
            if index % 3 != 0:
                tiles[index-1].change()
            if index % 3 != 2:
                tiles[index+1].change()
            if index >= 3:
                tiles[index-3].change()
            if index <= 5:
                tiles[index+3].change()
    judge()
'''
            if index == 0:
                tiles[1].change()
                tiles[3].change()
            elif index == 1:
                tiles[0].change()
                tiles[2].change()
                tiles[4].change()
            elif index == 2:
                tiles[1].change()
                tiles[5].change()
            elif index == 3:
                tiles[0].change()
                tiles[4].change()
                tiles[6].change()
            elif index == 4:
                tiles[1].change()
                tiles[2].change()
                tiles[5].change()
                tiles[7].change()
            elif index == 5:
                tiles[2].change()
                tiles[4].change()
                tiles[8].change()
            elif index == 6:
                tiles[3].change()
                tiles[7].change()
            elif index == 7:
                tiles[4].change()
                tiles[6].change()
                tiles[8].change()
            elif index == 8:
                tiles[5].change()
                tiles[7].change()
'''
finished = False
def reset():
    global finished, start
    for tile in tiles:
        tile.color = 'white' if random.randint(0,1) == 0 else 'black'
        cvs.itemconfig(tile.id,fill=tile.color)
    cvs.delete('result')
    start = time.time()
    finished = False

def judge():
    global finished
    w,b = 0,0
    for tile in tiles:
        if tile.color == 'white':
            w += 1
        else:
            b += 1
    if w == 9 or b == 9:
        cvs.create_text(cvs.winfo_width()/2,
            cvs.winfo_height()/2,
            text=f'全部消えた\n{time.time()-start:.2f} sec.',
            fill='red',font=('Helvetica',30),
            tags='result')
        finished = True

root = tkinter.Tk()
root.title('全部消しマス')
root.geometry('450x450')
root.bind('<Button>',pressed)
cvs = tkinter.Canvas(root,width=450,height=450,bg='white')
cvs.pack()
menu = tkinter.Menu(root)
menu1 = tkinter.Menu(menu,tearoff=0)
menu1.add_command(label='リセット',command=reset)
menu.add_cascade(label='実行',menu=menu1)
root.config(menu=menu)
start = time.time()
for t in tiles:
    t.draw()
root.mainloop()