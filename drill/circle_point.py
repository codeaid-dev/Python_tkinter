import tkinter

def motion(e):
    cvs.coords(id,e.x-50,e.y-50,e.x+50,e.y+50)
    if e.x<250 and e.y<250:
        cvs.itemconfig(id,fill='red')
    elif e.x>250 and e.y<250:
        cvs.itemconfig(id,fill='green')
    elif e.x<250 and e.y>250:
        cvs.itemconfig(id,fill='yellow')
    elif e.x>250 and e.y>250:
        cvs.itemconfig(id,fill='blue')

root = tkinter.Tk()
root.title('移動する円の色を変える')
root.bind('<Motion>',motion)
cvs = tkinter.Canvas(root, width=500, height=500, bg='black')
cvs.pack()

cvs.create_line(250,0,250,500,fill='white')
cvs.create_line(0,250,500,250,fill='white')
id = cvs.create_oval(200,200,300,300,fill='white',width=0)

root.mainloop()