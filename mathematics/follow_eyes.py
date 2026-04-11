import tkinter,math

mouseX,mouseY = 0,0
def motion(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y

root = tkinter.Tk()
root.title('目がマウスについていく')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

def follow_eye(x,y):
    cvs.create_oval(x-50,y-50,
                    x+50,y+50,
                    fill='white',width=0,
                    tags='shape')
    angle = math.atan2(mouseY-y, mouseX-x)
    ex = x+math.cos(angle)*20
    ey = y+math.sin(angle)*20
    cvs.create_oval(ex-25,ey-25,
                    ex+25,ey+25,
                    fill='black',width=0,
                    tags='shape')

def main():
    cvs.delete('shape')
    cvs.create_oval(0,0,
                    500,500,
                    fill='#4678C8',width=0,
                    tags='shape')
    follow_eye(150,250)
    follow_eye(350,250)

    root.after(10,main)

main()
root.mainloop()
