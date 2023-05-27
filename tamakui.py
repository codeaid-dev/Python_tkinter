import tkinter
import random

mouse_x,mouse_y = 0,0
player=None
enemy=[]
status=0
frame=0

class Circle:
    def __init__(self,x,y,size,color):
        self.x=x
        self.y=y
        self.size=size
        self.color=color
        self.id=None
    def draw(self):
        self.id = cvs.create_oval(self.x-self.size/2,self.y-self.size/2,self.x+self.size/2,self.y+self.size/2,fill=self.color,width=0)
        self.active=True
    def delete(self):
        if self.id:
            cvs.delete(self.id)
            self.active=False
    def move(self,x,y):
        self.x=x
        self.y=y
        cvs.coords(self.id,self.x-self.size/2,self.y-self.size/2,self.x+self.size/2,self.y+self.size/2)
    def colliderect(self,c):
        subx = abs(c.x-self.x)
        suby = abs(c.y-self.y)
        dist = (subx**2 + suby**2) ** 0.5
        return dist <= self.size/2 + c.size/2

def motion(e):
    global mouse_x,mouse_y
    mouse_x = e.x
    mouse_y = e.y

def press(e):
    global status
    if status == 0:
        cvs.delete('start')
        player.draw()
        status = 1

def create_enemy():
    c = f'#{random.randint(1,255):02x}{random.randint(1,255):02x}{random.randint(1,255):02x}'
    s = random.uniform(player.size*0.5,player.size*2)
    e = Circle(0,random.randint(0,400),s,c)
    e.speed = random.randint(-3,3)
    if e.speed == 0: e.speed = 1
    if e.speed < 0:
        e.x = 600
    e.draw()
    enemy.append(e)

def main():
    global frame,status
    if status == 0:
        cvs.create_text(300,200,text='GAME START',fill='white',font=('Times New Roman',30),tags='start')
    elif status == 1:
        player.move(mouse_x,mouse_y)
        frame+=1
    elif status == 2:
        fnt=('Times New Roman',30,'bold')
        cvs.create_text(300,200,text='GAME OVER',fill='white',font=fnt)
        return

    if frame != 0 and frame%50 == 0:
        create_enemy()
    for e in enemy:
        if e.active:
            e.move(e.x+e.speed,e.y)
            if player.colliderect(e):
                if player.size < e.size:
                    status=2
                else:
                    player.size += e.size*0.1
                    e.delete()
        if e.x < 0 or e.x > 600:
            e.delete()

    root.after(10, main)

root = tkinter.Tk()
root.title('玉食い')
root.bind('<Motion>', motion)
root.bind('<ButtonPress>', press)
root.geometry('600x400')
cvs = tkinter.Canvas(root, width=600, height=400, bg='black')
cvs.pack()
player=Circle(300,200,20,'white')
main()
root.mainloop()