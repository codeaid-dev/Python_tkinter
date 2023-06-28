import tkinter

x,y = 200,200

def key(e):
    global x,y
    if e.keysym == 'Left':
        x -= 5
        if x < 0:
            x += 5
    if e.keysym == 'Right':
        x += 5
        if x > 400:
            x -= 5
    if e.keysym == 'Up':
        y -= 5
        if y < 0:
            y += 5
    if e.keysym == 'Down':
        y += 5
        if y > 400:
            y -= 5
    cvs.coords('rect',x,y,x+100,y+100)

root = tkinter.Tk()
root.title('画面の中を四角形が移動')
root.bind('<Key>', key)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

cvs.create_rectangle(x,y,x+100,y+100,fill='blue',width=0, tag='rect')

root.mainloop()