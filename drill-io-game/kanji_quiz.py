import tkinter, random

kanji = {
    '薬':'images/kusuri.png',
    '粉':'images/fun2.png',
    '紛':'images/fun1.png',
    '語':'images/go.png',
    '話':'images/wa.png',
    '億':'images/oku3.png',
    '臆':'images/oku2.png',
    '憶':'images/oku1.png',
    '積':'images/seki2.png',
    '績':'images/seki1.png'
}
FONT = ('sans-serif', 16)
GRID_SIZE = 4
CELL_SIZE = 125
class Tile:
    pass

def select():
    keys = list(kanji.keys())
    return random.choice(keys)

def judge():
    global finished
    if finished:
        return
    if question == answer.get():
        if tiles.count(None) <= 3:
            point = 300
        elif tiles.count(None) <= 8:
            point = 250
        elif tiles.count(None) <= 13:
            point = 200
        else:
            point = 50
        result['text'] = f'正解！{point}ポイント'
    else:
        result['text'] = f"不正解（正解は{question}）"
    result.update()
    finished = True

def next():
    global question, img, tiles, finished
    if updateId != None:
        root.after_cancel(updateId)
    finished = False
    cvs.delete("all")
    result['text'] = '結果表示'
    result.update()
    question = select()
    img = tkinter.PhotoImage(file=kanji[question])
    cvs.create_image(250,250,image=img)
    tiles = []
    for i in range(16):
        t = Tile()
        t.x = i%GRID_SIZE*CELL_SIZE
        t.y = i//GRID_SIZE*CELL_SIZE
        tiles.append(t)
        t.id = cvs.create_rectangle(t.x,t.y,
                             t.x+CELL_SIZE,t.y+CELL_SIZE,
                             fill='gray',outline='black',
                             width=2)
    update()

def update():
    global finished, updateId
    if finished:
        return
    cell = random.randint(0,15)
    while tiles[cell] == None:
        cell = random.randint(0,15)
    cvs.delete(tiles[cell].id)
    cvs.update()
    tiles[cell] = None
    if tiles.count(None) == 16:
        result['text'] = f"時間切れ。。（正解は{question}）"
        result.update()
        finished = True
        return
    updateId = root.after(2000,update)

root = tkinter.Tk()
root.title('漢字クイズ')
cvs = tkinter.Canvas(root,width=500,height=500,bg='black')
cvs.pack()
result = tkinter.Label(root,
            text='結果表示',
            font=FONT)
result.pack(pady=10)
answer = tkinter.Entry(width=20,
            font=FONT)
answer.pack(pady=10)
btn1 = tkinter.Button(root,
        text='解答',
        font=FONT,
        command=judge)
btn1.pack(pady=10)
btn2 = tkinter.Button(root,
        text='次の問題',
        font=FONT,
        command=next)
btn2.pack(pady=10)

updateId = None
next()

root.mainloop()