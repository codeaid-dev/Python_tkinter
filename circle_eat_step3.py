import tkinter
import random

class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = 'white'
    def draw(self):
        self.id = cvs.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.color,width=0)
    def collide(self,c):
        subx = abs((c.x+c.size//2)-(self.x+self.size//2))
        suby = abs((c.y+c.size//2)-(self.y+self.size//2))
        dist = (subx**2 + suby**2) ** 0.5
        return dist <= self.size//2 + c.size//2

def motion(e):
    cvs.coords(player.id,e.x-player.size/2,e.y-player.size/2,
               e.x+player.size/2,e.y+player.size/2)
    player.x = e.x-player.size/2
    player.y = e.y-player.size/2

#step3
#Start game when mouse is clicked. Show the message in first display.
def press(e):
    global start
    if not start:
        start = True
        cvs.delete('start')
        main()

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

def main():
    global frame, over #step3 add over

    if over:
        cvs.create_text(300,200,text='GAME OVER',fill='white',font=('Times New Roman',30))
        return

    if frame%50==0:
        create_enemy()
    for i,e in enumerate(enemy): #step3 change to enumerate()
        e.x = e.x+e.speed
        cvs.coords(e.id,e.x,e.y,e.x+e.size,e.y+e.size)
        #step3
        if player.collide(e):
            if player.size < e.size:
                over = True
            else:
                player.size += e.size*0.1
                cvs.delete(e.id)
                del enemy[i]
                continue

        if e.x < -e.size or e.x > 600:
            cvs.delete(e.id)
            del enemy[i]

    frame += 1
    root.after(10, main)

player = None
enemy = []
frame = 1
#step3
start = False
over = False

root = tkinter.Tk()
root.title('円を食べる')
root.bind('<Motion>',motion)
root.bind('<ButtonPress>', press) #step3
cvs = tkinter.Canvas(root, width=600, height=400, bg='black')
cvs.pack()

player = Circle(300,200)
player.draw()
cvs.create_text(300,200,text='Click: GAME START',fill='white',font=('Times New Roman',30),tags='start')
#main() #step3 move to pressed function

root.mainloop()