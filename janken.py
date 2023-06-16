import tkinter, random

com = ['ぐー','ちょき','ぱー']

def click():
    c = random.choice(com)
    y = sv.get()
    if y == c:
      l['text'] = 'あいこ'
    elif (y == 'ぐー' and c == 'ちょき') or (y == 'ちょき' and c == 'ぱー') or (y == 'ぱー' and c == 'ぐー'):
       l['text'] = f'あなたの勝ち(コンピューター：{c})'
    elif (y == 'ぐー' and c == 'ぱー') or (y == 'ちょき' and c == 'ぐー') or (y == 'ぱー' and c == 'ちょき'):
       l['text'] = f'コンピューターの勝ち(コンピューター：{c})'

root = tkinter.Tk()
root.title('じゃんけん')
root.geometry('700x200')

f = tkinter.Frame(root)
f.pack()
sv = tkinter.StringVar()
sv.set('ぐー')
rb1 = tkinter.Radiobutton(f, text='ぐー', value='ぐー', variable=sv, font=('メイリオ',20))
rb2 = tkinter.Radiobutton(f, text='ちょき', value='ちょき', variable=sv, font=('メイリオ',20))
rb3 = tkinter.Radiobutton(f, text='ぱー', value='ぱー', variable=sv, font=('メイリオ',20))
rb1.grid(row=0, column=0)
rb2.grid(row=0, column=1)
rb3.grid(row=0, column=2)
b = tkinter.Button(root, text='ぽん', command=click, font=('メイリオ',20))
b.pack()
l = tkinter.Label(root, text='結果表示', font=('メイリオ',20))
l.pack()

root.mainloop()