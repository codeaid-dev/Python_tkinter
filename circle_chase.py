import tkinter

bx,by = 250,250
mx,my = 250,250

def move(e):
    global mx,my
    mx = e.x
    my = e.y

def main():
    global bx,by
    if bx < mx: bx += 5
    if mx < bx: bx -= 5
    if by < my: by += 5
    if my < by: by -= 5
    cvs.coords(ball,bx-25,by-25,bx+25,by+25)
    root.after(50,main)

root = tkinter.Tk()
root.title('ついてくる円')
root.bind('<Motion>',move)
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
ball = cvs.create_oval(bx-25,by-25,bx+25,by+25,fill='red',width=0)

main()
root.mainloop()