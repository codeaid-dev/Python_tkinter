import tkinter

def motion(e):
    cvs.coords(id,e.x-50,e.y-50,e.x+50,e.y+50)

root = tkinter.Tk()
root.title('マウスについていく円')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()
id = cvs.create_oval(0,0,
                    0,0,
                    fill='gray',
                    width=0,
                    tag='player')

root.mainloop()