import tkinter

FONT = ('Helvetica',18)
num_circle = 10

def show():
    try:
        num_circle = int(number.get())
    except ValueError:
        num_circle = 10
    size = 500/num_circle
    cvs.delete('all')
    for y in range(num_circle):
        for x in range(num_circle):
            cvs.create_oval(x*size, y*size,
                            x*size+size, y*size+size,
                            fill='black', width=0)

root = tkinter.Tk()
root.title('円を縦横に並べる②')

frame = tkinter.Frame(root)
label = tkinter.Label(frame, text='円の数: ',font=FONT)
label.grid(row=0, column=0)
number = tkinter.Entry(frame, width=10, font=FONT)
number.grid(row=0, column=1)
button = tkinter.Button(frame, text='表示', font=FONT, command=show)
button.grid(row=0, column=2)
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')

frame.pack()
cvs.pack()
show()
root.mainloop()
