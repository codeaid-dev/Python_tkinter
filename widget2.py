import tkinter

def click():
    txt = iv.get()
    l['text'] = txt

root = tkinter.Tk()
root.title('ラジオボタン')
root.geometry('400x200')

f = tkinter.Frame(root)
f.pack()
iv = tkinter.IntVar()
iv.set(1)
r1 = tkinter.Radiobutton(f, text='選択1', value=1, variable=iv, font=('メイリオ',20))
r1.grid(row=0, column=0)
r2 = tkinter.Radiobutton(f, text='選択2', value=2, variable=iv, font=('メイリオ',20))
r2.grid(row=0, column=1)
r3 = tkinter.Radiobutton(f, text='選択3', value=3, variable=iv, font=('メイリオ',20))
r3.grid(row=0, column=2)
b = tkinter.Button(root, text='表示', command=click, font=('メイリオ',24))
b.pack()
l = tkinter.Label(root, text='ここに表示', font=('メイリオ',32))
l.pack()

root.mainloop()