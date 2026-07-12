import tkinter
import random

class Rect:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.stat = random.randint(1,2)
        self.id=None
    def draw(self):
        self.id = cvs.create_rectangle(self.x,self.y,self.x+30,self.y+30,outline='black')
        self.change_color()
    def change_color(self):
        if self.id != None:
            if self.stat == 1:
                c = 'white'
            else:
                c = 'red'
            cvs.itemconfig(self.id,fill=c)

def press(e):
    if not complete:
        for i in range(25):
            if e.x>rects_r[i].x and e.x<rects_r[i].x+30 and e.y>rects_r[i].y and e.y<rects_r[i].y+30:
                if rects_r[i].stat == 1:
                    rects_r[i].stat = 2
                else:
                    rects_r[i].stat = 1
                rects_r[i].change_color()

def check():
    global complete
    same=0
    for i in range(25):
        if rects_l[i].stat == rects_r[i].stat:
            same += 1
    if same == 25:
        complete = True

def main():
    global timer
    if complete:
        cvs.create_text(250,100,text=f'COMPLETE!!:{timer/100:.2f}',fill='black',font=('Times New Roman',30))
        return
    timer += 1
    check()
    root.after(10, main)

root = tkinter.Tk()
root.title('同じ模様')
root.geometry('500x200')
root.bind('<ButtonPress>',press)
cvs = tkinter.Canvas(root, width=500, height=200, bg='gray')
cvs.pack()
complete = False
timer = 0
rects_r = []
rects_l = []
for i in range(25):
    left = Rect(50+i%5*30,25+int(i/5)*30)
    left.draw()
    rects_l.append(left)
    right = Rect(300+i%5*30,25+int(i/5)*30)
    right.draw()
    rects_r.append(right)
main()
root.mainloop()