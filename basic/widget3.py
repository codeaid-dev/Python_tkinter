import tkinter

def click():
    txt = ''
    txt += f'{bv[0].get()},{bv[1].get()},{bv[2].get()}'
    l['text'] = txt

root = tkinter.Tk()
root.title('チェックボックス')
root.geometry('400x200')

bv = [None] * 3
txt = ['選択1','選択2','選択3']
f = tkinter.Frame(root)
f.pack()
for i in range(len(txt)):
    bv[i] = tkinter.BooleanVar()
    bv[i].set(False)
    c = tkinter.Checkbutton(f, text=txt[i], variable=bv[i], font=('Helvetica',20))
    c.grid(row=0, column=i)
b = tkinter.Button(root, text='表示', command=click, font=('Helvetica',24))
b.pack()
l = tkinter.Label(root, text='ここに表示', font=('Helvetica',32))
l.pack()

root.mainloop()