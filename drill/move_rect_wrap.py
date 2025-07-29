import tkinter

x,y = 200,200

def key(e):
    global x,y
    if e.keysym == 'Left':
        x -= 15
        if x < -100:
            x = 500
    if e.keysym == 'Right':
        x += 15
        if x > 500:
            x = -100
    if e.keysym == 'Up':
        y -= 15
        if y < -100:
            y = 500
    if e.keysym == 'Down':
        y += 15
        if y > 500:
            y = -100
    cvs.coords('rect',x,y,x+100,y+100)

root = tkinter.Tk()
root.title('画面を超えて四角形が移動')
root.bind('<Key>', key)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

cvs.create_rectangle(x,y,x+100,y+100,fill='blue',width=0, tag='rect')

root.mainloop()