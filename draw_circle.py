import tkinter

root = tkinter.Tk()
root.title('円を描画')
cvs = tkinter.Canvas(root,width=500,
                    height=500,
                    bg='white')
cvs.create_oval(225,225,275,275,
                fill='black',
                width=0)
cvs.pack()
root.mainloop()
