import tkinter

def control(e):
    cvs.delete('player')
    cvs.create_oval(e.x-50,e.y-50,
                    e.x+50,e.y+50,
                    fill='gray',
                    width=0,
                    tags='player')

root = tkinter.Tk()
root.title('円を動かす')
root.bind('<Motion>', control)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

root.mainloop()