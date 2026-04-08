import tkinter

class Rectangle:
    pass

def motion(e):
    A.x = e.x-A.w/2
    A.y = e.y-A.h/2
    cvs.coords(A.id,A.x,A.y,A.x+A.w,A.y+A.h)

def main():
    if A.x <= B.x+B.w and A.x+A.w >= B.x and \
        A.y <= B.y+B.h and A.y+A.h >= B.y:
        cvs.itemconfig(B.id,fill='red')
    else:
        cvs.itemconfig(B.id,fill='black')
    root.after(10, main)

root = tkinter.Tk()
root.title('矩形(四角形)と矩形(四角形)の当たり判定')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
A = Rectangle()
A.x, A.y = 50, 50
A.w, A.h = 100, 100
A.id = cvs.create_rectangle(A.x,A.y,
            A.x+A.w,A.y+A.h,
            fill='green', width=0)
B = Rectangle()
B.x, B.y = 200, 200
B.w, B.h = 100, 100
B.id = cvs.create_rectangle(B.x,B.y,
            B.x+B.w,B.y+B.h,
            fill='black', width=0)
main()
root.mainloop()
