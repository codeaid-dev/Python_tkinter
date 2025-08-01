import tkinter

class Line:
    def __init__(self, prev, curr, width):
        self.x1, self.y1 = prev
        self.x2, self.y2 = curr
        self.width = width

lines = []
previous = None
stroke = 1

def press(e):
    global previous, stroke
    previous = (e.x, e.y)
    try:
        num = int(entry.get())
        if num > 0:
            stroke = num
        else:
            stroke = 1
    except ValueError:
        stroke = 1

def release(e):
    global previous
    previous = None

def drag(e):
    global previous
    current = (e.x, e.y)
    if previous:
        lines.append(Line(previous, current, stroke))
    previous = current
    for line in lines:
        cvs.create_line(line.x1,line.y1,
                        line.x2,line.y2,
                        fill='black',
                        width=line.width)

root = tkinter.Tk()
root.title('線の太さを入力してドラッグで描画')
root.geometry('500x500')
root.bind('<Button1-Motion>',drag)
root.bind('<Button-1>',press)
root.bind('<ButtonRelease>',release)

frame = tkinter.Frame(root)
frame.pack()
label = tkinter.Label(frame, text='線の太さ: ')
label.grid(row=0, column=0)
entry = tkinter.Entry(frame, width=10, font=('Helvetica',20))
entry.grid(row=0, column=1)

cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()

root.mainloop()