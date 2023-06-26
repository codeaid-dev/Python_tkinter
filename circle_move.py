import tkinter

x, y = 225, 225
speedx, speedy = 3, 2

def move():
    global x, y, speedx, speedy
    cvs.delete('circle')
    if x > 450 or x < 0:
        speedx *= -1
    if y > 450 or y < 0:
        speedy *= -1
    x += speedx
    y += speedy
    cvs.create_oval(x,y,x+50,y+50,
                    fill='black',
                    width=0,
                    tag='circle')
    root.after(10, move)

root = tkinter.Tk()
root.title('円を動かす')
cvs = tkinter.Canvas(root, width=500,
                    height=500,
                    bg='white')
cvs.pack()
move()
root.mainloop()