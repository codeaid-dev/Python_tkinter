import tkinter
import random

capital = {'ギリシャ':'アテネ','オランダ':'アムステルダム','オーストリア':'ウィーン','モンゴル':'ウランバートル','カナダ':'オタワ','エジプト':'カイロ','オーストラリア':'キャンベラ','スウェーデン':'ストックホルム','日本':'東京','インド':'ニューデリー','ベトナム':'ハノイ','フランス':'パリ','ドイツ':'ベルリン','イギリス':'ロンドン','アメリカ':'ワシントン'}

question = random.choice(list(capital.keys()))

root = tkinter.Tk()
root.geometry('600x400')
q = tkinter.Label(root,
    text=f'{question}の首都はどこ？',
    font=('メイリオ', '24'))
e = tkinter.Entry(root,
    width=10,
    font=('メイリオ', '24'))

def judge():
    if e.get() == capital[question]:
        result['text'] = f'正解!!'
    else:
        result['text'] = f'不正解:正解は{capital[question]}'
    result.update()

btn = tkinter.Button(root,
    text='解答',
    font=('メイリオ', '24'),
    command=judge)
result = tkinter.Label(root,
    text='',
    font=('メイリオ', '24'))
q.pack(pady=10)
e.pack(pady=10)
btn.pack(pady=10)
result.pack(pady=10)

root.mainloop()
