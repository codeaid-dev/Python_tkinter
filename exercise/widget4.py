import tkinter

def click():
    l['text'] = sv.get()

root = tkinter.Tk()
root.title('プルダウンメニュー')
root.geometry('400x200')

txt = ['選択1','選択2','選択3']
sv = tkinter.StringVar()
sv.set(txt[0])
o = tkinter.OptionMenu(root, sv, *txt)
o.config(font=('Helvetica',20))
o.pack()
b = tkinter.Button(root, text='表示', command=click, font=('Helvetica',24))
b.pack()
l = tkinter.Label(root, text='ここに表示', font=('Helvetica',32))
l.pack()

root.mainloop()