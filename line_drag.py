import tkinter

x,y = 0,0
def press(e):
    global x,y
    x = e.x
    y = e.y
def drag(e):
    global x,y
    cvs.create_line(x,y,e.x,e.y,fill='black',width=2)
    x = e.x
    y = e.y

root = tkinter.Tk()
root.title('ドラッグして線を描く')
root.geometry('500x500')
root.bind('<Button1-Motion>',drag)
root.bind('<Button-1>',press)
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()

root.mainloop()