import tkinter

x, y = 0, 0
status = 0

def move():
    global x, y, status
    if status == 0:
        x += 1
        if x > 400:
            status = 1
            x = 400
    if status == 1:
        y += 1
        if y > 400:
            status = 2
            y = 400
    if status == 2:
        x -= 1
        if x < 0:
            status = 3
            x = 0
    if status == 3:
        y -= 1
        if y < 0:
            status = 0
            y = 0
    cvs.coords('rect',x,y,x+100,y+100)
    root.after(10, move)

root = tkinter.Tk()
root.title('画面端に沿って四角形が移動')
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
cvs.create_rectangle(x,y,x+100,y+100,fill='blue',width=0, tag='rect')

move()
root.mainloop()
