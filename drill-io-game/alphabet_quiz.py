import tkinter
import random, time

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
question = ''
FONT = ('Helvetica', '24')

atari = random.randint(0,25)
for i in range(26):
    if i == atari:
        continue
    question += alphabet[i]

root = tkinter.Tk()
root.geometry('600x400')
root.title('アルファベットクイズ')
q1 = tkinter.Label(root, text='抜けているアルファベットはどれ？', font=FONT)
q2 = tkinter.Label(root, text=question, font=FONT, fg='#800000', bg='#808080')
e = tkinter.Entry(root, width=5, font=FONT)

def check():
    if e.get().upper() in alphabet:
        if e.get().upper() in question:
            result['text'] = f'不正解:正解は{alphabet[atari]}'
        else:
            spend = time.time() - start
            result['text'] = f'正解!({spend:.1f}秒)'
    else:
        result['text'] = 'アルファベットを入力してください'
    result.update()

btn = tkinter.Button(root, text='解答', font=FONT, command=check)
result = tkinter.Label(root, text='', font=FONT)
q1.pack(pady=10)
q2.pack(pady=10)
e.pack(pady=10)
btn.pack(pady=10)
result.pack(pady=10)

start = time.time()

root.mainloop()