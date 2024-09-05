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

def select():
    keys = list(kanji.keys())
    return random.choice(keys)

root = tkinter.Tk()
root.title('漢字クイズ')
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
question = select()
img = tkinter.PhotoImage(file=kanji[question])
cvs.create_image(0,0,image=img)