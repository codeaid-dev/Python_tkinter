import tkinter, random

bs = 100
by = (200-bs)/2
space = (900-bs*5)//6
atari = random.randint(0,4)

def pressed(e):
    for i in range(5):
        if i*(bs+space)+space<e.x<i*(bs+space)+space+bs and by<e.y<by+bs:
            if i == atari:
                cvs.create_oval(i*(bs+space)+space,by,
                        i*(bs+space)+space+bs,by+bs,
                        fill='red',width=0)

root = tkinter.Tk()
root.title('当たりを探せ①')
root.bind('<Button>', pressed)
cvs = tkinter.Canvas(root, width=900, height=200, bg='white')
cvs.pack()
for i in range(5):
    cvs.create_rectangle(i*(bs+space)+space,by,
                i*(bs+space)+space+bs,by+bs,
                fill='black',width=0)

root.mainloop()