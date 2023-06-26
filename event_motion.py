import tkinter

def control(e):
    cvs.coords(id,e.x-50,e.y-50,e.x+50,e.y+50)

root = tkinter.Tk()
root.title('円を動かす')
root.bind('<Motion>', control)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
id = cvs.create_oval(-100,-100,
                    0,0,
                    fill='gray',
                    width=0,
                    tag='player')

root.mainloop()