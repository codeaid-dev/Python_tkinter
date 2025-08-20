import tkinter
import random

capital = {'ギリシャ':'アテネ','オランダ':'アムステルダム','オーストリア':'ウィーン','モンゴル':'ウランバートル','カナダ':'オタワ','エジプト':'カイロ','オーストラリア':'キャンベラ','スウェーデン':'ストックホルム','日本':'東京','インド':'ニューデリー','ベトナム':'ハノイ','フランス':'パリ','ドイツ':'ベルリン','イギリス':'ロンドン','アメリカ':'ワシントン'}
FONT = ('sans-serif', '24')

question = random.choice(list(capital.keys()))

root = tkinter.Tk()
root.geometry('600x400')
root.title('首都クイズ')
q = tkinter.Label(root,
    text=f'{question}の首都はどこ？',
    font=FONT)
e = tkinter.Entry(root,
    width=10,
    font=FONT)

def judge():
    if e.get() == capital[question]:
        result['text'] = f'正解!!'
    else:
        result['text'] = f'不正解:正解は{capital[question]}'
    result.update()

btn = tkinter.Button(root,
    text='解答',
    font=FONT,
    command=judge)
result = tkinter.Label(root,
    text='',
    font=FONT)
q.pack(pady=10)
e.pack(pady=10)
btn.pack(pady=10)
result.pack(pady=10)

root.mainloop()
