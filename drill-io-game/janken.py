import tkinter
import random

FONT = ('sans-serif', 20)
images = []
def pon():
    #0:グー、1:チョキ、2:パー
    global comimg,youimg,com,you
    cvs.delete('result')
    cvs.delete(comimg)
    cvs.delete(youimg)
    c = random.randint(0,2)
    y = intvar.get()
    com = images[c].subsample(2)
    you = images[y].subsample(2)
    comimg = cvs.create_image(125,125,image=com)
    youimg = cvs.create_image(375,125,image=you)
    if (c==0 and y==1) or (c==1 and y==2) or (c==2 and y==0):
        cvs.create_text(250,125,text='コンピューターの勝ち',fill='black',font=('Helvetica',20),tags='result')
    elif (c==0 and y==2) or (c==1 and y==0) or (c==2 and y==1):
        cvs.create_text(250,125,text='あなたの勝ち',fill='black',font=('Helvetica',20),tags='result')
    else:
        cvs.create_text(250,125,text='あいこ',fill='black',font=('Helvetica',20),tags='result')

root = tkinter.Tk()
root.title('じゃんけん')
cvs = tkinter.Canvas(root, width=500, height=250, bg='white')
cvs.pack()
images.append(tkinter.PhotoImage(file='images/janken_gu.png'))
images.append(tkinter.PhotoImage(file='images/janken_choki.png'))
images.append(tkinter.PhotoImage(file='images/janken_pa.png'))

com = images[0].subsample(2)
comimg = cvs.create_image(125,125,image=com)
you = images[0].subsample(2)
youimg = cvs.create_image(375,125,image=you)

btn = tkinter.Button(root, text='ぽん', font=FONT, command=pon)
btn.pack(side=tkinter.BOTTOM, pady=10)

frm = tkinter.Frame(root)
frm.pack(side=tkinter.BOTTOM)
intvar = tkinter.IntVar()
intvar.set(0)
rb1 = tkinter.Radiobutton(frm, text='グー', value=0, variable=intvar, font=FONT)
rb2 = tkinter.Radiobutton(frm, text='チョキ', value=1, variable=intvar, font=FONT)
rb3 = tkinter.Radiobutton(frm, text='パー', value=2, variable=intvar, font=FONT)
rb1.grid(row=0, column=0)
rb2.grid(row=0, column=1)
rb3.grid(row=0, column=2)

root.mainloop()