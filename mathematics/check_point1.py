import tkinter,math

def motion(e):
    global mx, my
    mx = e.x
    my = e.y

def main():
    cvs.delete('shape')
    draw_guide()
    angle = math.atan2(my-centerY, mx-centerX)
    x = centerX+200*math.cos(angle)
    y = centerY+200*math.sin(angle)
    cvs.create_line(centerX, centerY, x, y,
                    fill='black', tags='shape',
                    width=2)
    cvs.create_oval(x-5, y-5, x+5, y+5,
                    fill='black', tags='shape',
                    width=0)
    root.after(10,main)

def draw_guide():
    cvs.create_oval(centerX-200, centerY-200,
                    centerX+200, centerY+200,
                    fill='white', tags='shape',
                    outline='lightgray', width=2)
    cvs.create_line(centerX, centerY-200,
                    centerX, centerY+200,
                    fill='lightgray', tags='shape',
                    width=2)
    cvs.create_line(centerX-200, centerY,
                    centerX+200, centerY,
                    fill='lightgray', tags='shape',
                    width=2)

root = tkinter.Tk()
root.title('円周上の座標確認')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

centerX, centerY = 250, 250
mx, my = 0, 0

main()
root.mainloop()
