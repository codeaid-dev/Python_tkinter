import tkinter
import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
question = ''

atari = random.randint(0,25)
for i in range(26):
    if i == atari:
        continue
    question += alphabet[i]

root = tkinter.Tk()
root.geometry('600x400')
q1 = tkinter.Label(root,
    text='抜けているアルファベットはどれ？',
    font=('メイリオ', '24'))
q2 = tkinter.Label(root,
        text=question,
        font=('メイリオ', '24'),
        fg='#800000',
        bg='#808080')
e = tkinter.Entry(root,
        width=5,
        font=('メイリオ', '24'))

def check():
    if e.get().upper() in alphabet:
        if e.get().upper() in question:
            result['text'] = f'不正解:正解は{alphabet[atari]}'
        else:
            result['text'] = '正解!'
    else:
        result['text'] = 'アルファベットを入力してください'
    result.update()

btn = tkinter.Button(root,
        text='解答',
        font=('メイリオ', '24'), command=check)
result = tkinter.Label(root,
        text='',
        font=('メイリオ', '24'))
q1.pack(pady=10)
q2.pack(pady=10)
e.pack(pady=10)
btn.pack(pady=10)
result.pack(pady=10)

root.mainloop()