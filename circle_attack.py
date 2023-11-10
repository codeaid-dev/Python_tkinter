import tkinter,random

bx,by = 250,250
dx,dy = 0,0
score = 0
count = 0
over = False

def pressed(event):
    global score
    dist = ((bx-event.x)**2+(by-event.y)**2)**0.5
    if dist < 25:
        score += 1

def main():
    global bx,by,dx,dy,count,over
    if over:
        return
    if count % 100 == 0:
        nx = random.randint(25,475)
        ny = random.randint(25,475)
        dx = (nx-bx)/100
        dy = (ny-by)/100
    count += 1
    if count >= 1000:
        over = True
        cvs.create_text(250,50,text='GAME OVER',fill='red',font=('メイリオ',40))
    bx += dx
    by += dy
    cvs.coords(ball,bx-25,by-25,bx+25,by+25)
    cvs.delete('score')
    cvs.create_text(250,250,text=f'Score:{score}',fill='black',font=('メイリオ',40),tags='score')
    root.after(10,main)

root = tkinter.Tk()
root.title('円たたき')
root.bind('<Button>', pressed)
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
ball = cvs.create_oval(bx-25,by-25,bx+25,by+25,fill='red',width=0)
cvs.create_text(250,250,text=f'Score:{score}',fill='white',font=('メイリオ',40),tags='score')
main()
root.mainloop()