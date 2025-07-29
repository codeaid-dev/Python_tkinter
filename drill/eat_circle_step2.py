import tkinter
import random #step2

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

#step2
def create_enemy():
    c = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
    s = random.uniform(player.size*0.5,player.size*2)
    e = Circle(-s,random.uniform(0,400-s))
    e.size = s
    e.color = c
    e.speed = random.randint(-3,3)
    if e.speed == 0:
        e.speed = 1
    if e.speed < 0:
        e.x = 600
    e.draw()
    enemy.append(e)

#step2
def main():
    global frame

    if frame%50==0:
        create_enemy()
    for e in enemy:
        e.x = e.x+e.speed
        cvs.coords(e.id,e.x,e.y,e.x+e.size,e.y+e.size)

    frame += 1
    root.after(10, main)

player = None
#step2
enemy = []
frame = 1

root = tkinter.Tk()
root.title('円を食べる')
root.bind('<Motion>',motion)
cvs = tkinter.Canvas(root, width=600, height=400, bg='black')
cvs.pack()

player = Circle(300,200)
player.draw()
main() #step2

root.mainloop()