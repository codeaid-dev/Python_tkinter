import tkinter

x,y = 0,0
id = 0
def press(e):
    global x,y,id
    x = e.x
    y = e.y
    id = cvs.create_oval(x,y,x,y,fill='yellow',width=0)
def drag(e):
    dst = ((e.x-x)**2 + (e.y-y)**2) ** 0.5
    cvs.coords(id,x-dst,y-dst,x+dst,y+dst)

root = tkinter.Tk()
root.title('ドラッグして円を描く(改造)')
root.geometry('500x500')
root.bind('<Button1-Motion>',drag)
root.bind('<Button-1>',press)
cvs = tkinter.Canvas(root,width=500,height=500,bg='black')
cvs.pack()

root.mainloop()