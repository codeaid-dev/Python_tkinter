import tkinter
import random

national_flags = {'ベルギー':'./images/Belgium.png',
                  'ブルガリア':'./images/Bulgaria.png',
                  'デンマーク':'./images/Denmark.png',
                  'フィンランド':'./images/Finland.png',
                  'ドイツ':'./images/Germany.png',
                  'ハンガリー':'./images/Hungary.png',
                  'イタリア':'./images/Italy.png',
                  'モナコ':'./images/Monaco.png',
                  'ボーランド':'./images/Poland.png',
                  'スウェーデン':'./images/Sweden.png'}

def select():
    keys = list(national_flags.keys())
    return random.choice(keys)

def judge():
    if correct == answer.get():
        result['text'] = '正解！'
    else:
        result['text'] = f"不正解（正解は{correct}）"
    result.update()

def next():
    global correct, img
    correct = select()
    img = tkinter.PhotoImage(file=national_flags[correct])
    question['image'] = img
    question.update()
    result['text'] = '結果表示'

root = tkinter.Tk()
root.title('国旗クイズ')

correct = select()
img = tkinter.PhotoImage(file=national_flags[correct])
question = tkinter.Label(root, image=img)
question.pack()
result = tkinter.Label(root,
            text='結果表示',
            font=('メイリオ', 16))
result.pack(pady=10)
answer = tkinter.Entry(width=20,
            font=('メイリオ', 16))
answer.pack(pady=10)
btn1 = tkinter.Button(root,
        text='解答',
        font=('メイリオ', 16),
        command=judge)
btn1.pack(pady=10)
btn2 = tkinter.Button(root,
        text='次の問題',
        font=('メイリオ', 16),
        command=next)
btn2.pack(pady=10)

root.mainloop()