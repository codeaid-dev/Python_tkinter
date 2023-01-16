import tkinter

x,y = 200,200

def key(e):
    global x,y
#    cvs.delete('rect')
    if e.keysym == 'Left':
        x -= 5
    if e.keysym == 'Right':
        x += 5
    if e.keysym == 'Up':
        y -= 5
    if e.keysym == 'Down':
        y += 5
    cvs.coords('rect',x,y,x+100,y+100)
#    cvs.create_rectangle(x,y,x+100,y+100,fill='blue',width=0, tag='rect')

root = tkinter.Tk()
root.title('図形を動かす')
root.bind('<Key>', key)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

cvs.create_rectangle(x,y,x+100,y+100,fill='blue',width=0, tag='rect')

root.mainloop()