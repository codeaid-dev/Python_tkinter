import tkinter

x, y = [75,225,325], [225,225,225]
speedx, speedy = [3,2,3], [2,3,1]
def move():
#    global x, y, speedx, speedy
    cvs.delete('circle')
    for i in range(3):
        if x[i] > 450 or x[i] < 0:
            speedx[i] *= -1
        if y[i] > 450 or y[i] < 0:
            speedy[i] *= -1
        x[i] += speedx[i]
        y[i] += speedy[i]
        cvs.create_oval(x[i],y[i],x[i]+50,y[i]+50,fill='black',width=0,tags='circle')
    root.after(10, move)

root = tkinter.Tk()
root.title('円を動かす')
#root.geometry('500x500')

cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

move()
#cvs.create_oval(x,y,x+50,y+50,fill='black',width=0,tags='circle')

root.mainloop()