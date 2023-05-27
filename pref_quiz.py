import json
import tkinter
import random

with open('prefectures.json', 'r', encoding='utf-8') as f:
    prefs = json.loads(f.read())

correct = None
def questions():
    global correct
    correct = random.randint(0,len(prefs)-1)
    q['image'] = prefs[correct]['img']
    q.update()
    result['text'] = '結果表示'

def judge():
    if prefs[correct]['pref'] == answer.get():
        result['text'] = '正解！'
    else:
        result['text'] = f"不正解（正解は{prefs[correct]['pref']}）"
    result.update()

root = tkinter.Tk()
root.title('都道府県クイズ')

for d in prefs:
    d['img'] = tkinter.PhotoImage(file=d['file'])

q = tkinter.Label(root, image=prefs[0]['img'])
q.pack()
btn1 = tkinter.Button(root,
        text='次の問題',
        font=('メイリオ', 16),
        command=questions)
btn1.pack(side=tkinter.BOTTOM, pady=10)
btn2 = tkinter.Button(root,
        text='解答',
        font=('メイリオ', 16),
        command=judge)
btn2.pack(side=tkinter.BOTTOM, pady=10)
answer = tkinter.Entry(width=20,
            font=('メイリオ', 16))
answer.pack(side=tkinter.BOTTOM, pady=10)
result = tkinter.Label(root,
            text='結果表示',
            font=('メイリオ', 16))
result.pack(side=tkinter.BOTTOM)

questions()
root.mainloop()
