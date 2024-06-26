import tkinter
import random

omikuji = []

def uranai():
    result = random.randint(1,100)
    if 1 <= result <= 2:
        num = 0
    elif 3 <= result <= 12:
        num = 1
    elif 13 <= result <= 32:
        num = 2
    elif 23 <= result <= 62:
        num = 3
    elif 53 <= result <= 82:
        num = 4
    elif 73 <= result <= 92:
        num = 5
    else:
        num = 6
    cvs.itemconfig(kuji,image=omikuji[num])

root = tkinter.Tk()
root.title('おみくじ')
cvs = tkinter.Canvas(root, width=300, height=300, bg='white')
cvs.pack()
for i in range(1,8):
    omikuji.append(tkinter.PhotoImage(file=f'images/omikuji_fuda{i}.png'))

box = tkinter.PhotoImage(file='images/omikuji.png')
kuji = cvs.create_image(150,150, image=box)
button = tkinter.Button(root, text='おみくじを引く', font=('メイリオ', 20), command=uranai)
button.pack(side=tkinter.BOTTOM, pady=10)
root.mainloop()
