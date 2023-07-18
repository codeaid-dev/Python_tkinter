import tkinter

class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = 'white'
    def draw(self):
        self.id = cvs.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.color,width=0)

def motion(e):
    cvs.coords(player.id,e.x-player.size/2,e.y-player.size/2,
               e.x+player.size/2,e.y+player.size/2)
    player.x = e.x-player.size/2
    player.y = e.y-player.size/2

player = None
status = 0

root = tkinter.Tk()
root.title('円を食べる')
root.bind('<Motion>',motion)
cvs = tkinter.Canvas(root, width=600, height=400, bg='black')
cvs.pack()

player = Circle(300,200)
player.draw()

root.mainloop()