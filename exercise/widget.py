import tkinter

def click():
    txt = e.get()
    l['text'] = txt

root = tkinter.Tk()
root.title('フォーム')
root.geometry('400x400')

e = tkinter.Entry(root, width=10, font=('Helvetica',32))
e.pack()
b = tkinter.Button(root, text='表示', command=click, font=('Helvetica',32))
b.pack()
l = tkinter.Label(root, text='ここに表示', font=('Helvetica',32))
l.pack()

root.mainloop()