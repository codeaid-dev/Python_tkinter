import tkinter
import random
import time

masu = [[0 for x in range(10)] for y in range(10)]
atari = (random.randint(0,9),random.randint(0,9))
#masu = [0 for i in range(100)]
#atari = random.randint(0,99)
clear = False
print(atari)

def click(e):
    global clear,end
    x = e.x // 50
    y = e.y // 50
    if x==atari[0] and y==atari[1]:
    #if x == atari%10 and y == atari//10:
        if not clear:
            end = time.time()-start
            clear = True
        cvs.create_oval(x*50,y*50,x*50+50,y*50+50,fill='red')
        cvs.create_text(250,250,text=f'経過時間：{end:.0f}秒',fill='black',font=('Helvetica',32))

root = tkinter.Tk()
root.title('当たりを探せ②')
root.geometry('500x500')
root.bind('<Button>',click)
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
for y in range(10):
    for x in range(10):
        cvs.create_rectangle(x*50,y*50,x*50+50,y*50+50,fill='gray')
start = time.time()

root.mainloop()