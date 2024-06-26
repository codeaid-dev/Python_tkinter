import tkinter

def click():
    txt = iv.get()
    l['text'] = txt

root = tkinter.Tk()
root.title('ラジオボタン')
root.geometry('400x200')

txt = ['選択1','選択2','選択3']
f = tkinter.Frame(root)
f.pack()
iv = tkinter.IntVar()
iv.set(1)
for i in range(len(txt)):
    r = tkinter.Radiobutton(f, text=txt[i], value=i+1, variable=iv, font=('メイリオ',20))
    r.grid(row=0, column=i)
b = tkinter.Button(root, text='表示', command=click, font=('メイリオ',24))
b.pack()
l = tkinter.Label(root, text='ここに表示', font=('メイリオ',32))
l.pack()

root.mainloop()