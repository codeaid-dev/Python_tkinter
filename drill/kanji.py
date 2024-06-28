import tkinter
import random, time

class Rect:
    def __init__(self,x,y):
        self.x = x
        self.y = y

tiles = []
questions = {'方':'万','楜':'湖','紛':'粉','夭':'天'}
over = False

def pressed(event):
    global over
    if over:
        return
    for tile in tiles:
        if tile.x < event.x < tile.x+50 and tile.y < event.y < tile.y+50:
            if tile.atari:
                spend = time.time()-start
                cvs.itemconfig(tile.id, fill='red')
                cvs.create_text(250,250,text='FINISH!!',fill='white',font=('Helvetica', 30))
                cvs.create_text(250,300,text=f'{spend:.1f}',fill='white',font=('Helvetica', 30))
                over = True
    cvs.update()


root = tkinter.Tk()
root.title('違う漢字はどれ？')
root.geometry('500x500')
root.bind('<Button>',pressed)
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
atari = random.randint(0,99)
qkey = random.choice(list(questions.keys()))
for i in range(100):
    x = i%10*50
    y = i//10*50
    tile = Rect(x,y)
    tile.id = cvs.create_rectangle(x,y,x+50,y+50,fill='gray')
    if i == atari:
        cvs.create_text(x+25,y+25,text=qkey,fill='black',font=('Helvetica', 18))
        tile.atari = True
    else:
        cvs.create_text(x+25,y+25,text=questions[qkey],fill='black',font=('Helvetica', 18))
        tile.atari = False
    tiles.append(tile)

start = time.time()

root.mainloop()