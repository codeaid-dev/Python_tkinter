import tkinter

def motion(e):
    cvs.delete('signal')
    if e.x < 300:
        cvs.create_oval(0,0,300,300,fill='green',width=0,tags='signal')
    if 300 <= e.x < 600:
        cvs.create_oval(300,0,600,300,fill='yellow',width=0,tags='signal')
    if 600 <= e.x < 900:
        cvs.create_oval(600,0,900,300,fill='red',width=0,tags='signal')

root = tkinter.Tk()
root.title('信号機')
root.bind('<Motion>',motion)
cvs = tkinter.Canvas(root, width=900,
                    height=300,
                    bg='white')
cvs.pack()

root.mainloop()