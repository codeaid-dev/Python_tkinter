import tkinter

x,y = 200,200

def key(e):
    global x,y
    if e.keysym == 'Left':
        x -= 15
        if x < 0:
            x = 0
    if e.keysym == 'Right':
        x += 15
        if x > 400:
            x = 400
    if e.keysym == 'Up':
        y -= 15
        if y < 0:
            y = 0
    if e.keysym == 'Down':
        y += 15
        if y > 400:
            y = 400
    cvs.coords('rect',x,y,x+100,y+100)

root = tkinter.Tk()
root.title('キーで四角形を動かす')
root.bind('<Key>', key)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

cvs.create_rectangle(x,y,x+100,y+100,fill='blue',width=0, tag='rect')

root.mainloop()