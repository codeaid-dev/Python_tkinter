import tkinter,math

mouseX,mouseY = 0,0
def motion(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y

root = tkinter.Tk()
root.title('マウスについていく円')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

followX,followY=450,450

def draw_sin_cos():
    cvs.create_line(followX,followY,
                    mouseX,mouseY,fill='black',
                    width=1,
                    tags='shape')
    cvs.create_line(followX,followY,
                    followX,mouseY,
                    fill='#00C800',
                    width=5,tags='shape')
    cvs.create_line(followX,followY,
                    mouseX,followY,
                    fill='#FFAF00',
                    width=5,tags='shape')

def show_degrees(angle):
    angle = (angle+2*math.pi)%(2*math.pi)
    cvs.create_text(250,400,
                    text=f'{int(math.degrees(angle))} degrees',
                    fill='black',font=('Helvetica',20),
                    tags='shape')
    cvs.create_text(250,450,
                    text=f'{int(angle*100)/100} radians',
                    fill='black',font=('Helvetica',20),
                    tags='shape')

def follow_circle():
    global followX, followY
    dx = mouseX - followX
    dy = mouseY - followY
    angle = math.atan2(dy,dx)
    dist = ((followX - mouseX)**2 + (followY - mouseY)**2)**0.5
    if dist >= 1:
        followX += math.cos(angle)*2
        followY += math.sin(angle)*2
    cvs.create_oval(followX-10,followY-10,
                    followX+10,followY+10,
                    fill='red',width=0,
                    tags='shape')
    show_degrees(angle)


def main():
    cvs.delete('shape')
    cvs.create_oval(mouseX-5,mouseY-5,
                    mouseX+5,mouseY+5,
                    fill='black',width=0,
                    tags='shape')
    draw_sin_cos()
    follow_circle()
    root.after(10,main)

main()
root.mainloop()
