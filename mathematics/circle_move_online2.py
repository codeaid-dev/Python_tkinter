import tkinter,math

root = tkinter.Tk()
root.title('線上で円が移動する')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

x1,y1, = 100,100
x2,y2 = 400,400
circleX,circleY = x1,y1
target = (x2,y2)
speed = 2
def main():
    global circleX,circleY,target
    cvs.delete('circle')
    tx,ty = target
    dx = tx - circleX
    dy = ty - circleY
    dist = (dx**2 + dy**2)**0.5
    if dist < speed:
        circleX, circleY = tx, ty
        if target == (x2, y2):
            target = (x1, y1)
        else:
            target = (x2, y2)
    else:
        angle = math.atan2(dy,dx)
        circleX += math.cos(angle)*speed
        circleY += math.sin(angle)*speed
        # circleX += dx / dist * speed
        # circleY += dy / dist * speed

    cvs.create_oval(circleX-30,circleY-30,
                    circleX+30,circleY+30,
                    fill='black',width=0,
                    tags='circle')
    root.after(10,main)

cvs.create_line(x1,y1,x2,y2,
                fill='black')

main()
root.mainloop()