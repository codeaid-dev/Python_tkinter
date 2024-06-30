import tkinter

FONT = ('Helvetica',32)

def create():
    r = 1 if bv[0].get() else 0
    g = 2 if bv[1].get() else 0
    b = 4 if bv[2].get() else 0
    color = r+g+b
    if color == 1:
        l['text'] = '作れる色は：赤'
    elif color == 2:
        l['text'] = '作れる色は：緑'
    elif color == 3:
        l['text'] = '作れる色は：黄'
    elif color == 4:
        l['text'] = '作れる色は：青'
    elif color == 5:
        l['text'] = '作れる色は：マゼンタ'
    elif color == 6:
        l['text'] = '作れる色は：シアン'
    elif color == 7:
        l['text'] = '作れる色は：白'
    else:
        l['text'] = '作れる色は：黒'

root = tkinter.Tk()
root.title('選択した色を表示')
root.geometry('400x200')

bv = [None] * 3
colors = ['赤','緑','青']
f = tkinter.Frame(root)
f.pack(pady=5)
for i in range(len(colors)):
    bv[i] = tkinter.BooleanVar()
    bv[i].set(False)
    c = tkinter.Checkbutton(f, text=colors[i],
                            variable=bv[i],
                            font=('Helvetica',20))
    c.grid(row=0, column=i)
b = tkinter.Button(root, text='作れる色', command=create, font=('Helvetica',24))
b.pack()
l = tkinter.Label(root, text='ここに表示', font=('Helvetica',24))
l.pack()

root.mainloop()