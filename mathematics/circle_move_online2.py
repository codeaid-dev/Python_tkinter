import tkinter,math

root = tkinter.Tk()
root.title('線上で円が移動する')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

x1,y1, = 100,100
x2,y2 = 400,400
circleX,circleY = x1,y1
status = True
def main():
    global circleX,circleY,status
    cvs.delete('circle')
    if status:
        dx = x2 - circleX
        dy = y2 - circleY
        dist = ((circleX - x2)**2+(circleY - y2)**2)**0.5
        if dist < 1:
            status = False
    else:
        dx = x1 - circleX
        dy = y1 - circleY
        dist = ((circleX - x1)**2+(circleY - y1)**2)**0.5
        if dist < 1:
            status = True

    angle = math.atan2(dy,dx)
    circleX += math.cos(angle)*2
    circleY += math.sin(angle)*2

    cvs.create_oval(circleX-30,circleY-30,
                    circleX+30,circleY+30,
                    fill='black',width=0,
                    tags='circle')
    root.after(10,main)

cvs.create_line(x1,y1,x2,y2,
                fill='black')

main()
root.mainloop()