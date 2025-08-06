import tkinter

class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def judge():
    for i in range(len(masu)):
        if 0<=i%7<=3:
            if masu[i].stat==1 and masu[i+1].stat==1 and masu[i+2].stat==1 and masu[i+3].stat==1:
                return 1
            if masu[i].stat==2 and masu[i+1].stat==2 and masu[i+2].stat==2 and masu[i+3].stat==2:
                return 2
        if 0<=i//7<=2:
            if masu[i].stat==1 and masu[i+7].stat==1 and masu[i+14].stat==1 and masu[i+21].stat==1:
                return 1
            if masu[i].stat==2 and masu[i+7].stat==2 and masu[i+14].stat==2 and masu[i+21].stat==2:
                return 2
        if 3<=i<=6 or 10<=i<=13 or 17<=i<=20:
            if masu[i].stat==1 and masu[i+6].stat==1 and masu[i+12].stat==1 and masu[i+18].stat==1:
                return 1
            if masu[i].stat==2 and masu[i+6].stat==2 and masu[i+12].stat==2 and masu[i+18].stat==2:
                return 2
        if 0<=i<=3 or 7<=i<=10 or 14<=i<=17:
            if masu[i].stat==1 and masu[i+8].stat==1 and masu[i+16].stat==1 and masu[i+24].stat==1:
                return 1
            if masu[i].stat==2 and masu[i+8].stat==2 and masu[i+16].stat==2 and masu[i+24].stat==2:
                return 2
    return 0

over = False
turn = False # True:赤,False:黄
masu = []
def pressed(event):
    global turn,over
    if over:
        return
    for i,en in enumerate(masu):
        if en.x < event.x < en.x+100 and en.y < event.y < en.y+100:
            if (i>=35 and en.stat==0) or (i<35 and masu[i+7].stat!=0 and en.stat==0):
                if turn:
                  cvs.itemconfig(en.id,fill='red')
                  turn = False
                  en.stat = 1
                else:
                  cvs.itemconfig(en.id,fill='yellow')
                  turn = True
                  en.stat = 2
        if judge() == 1:
            cvs.create_text(350,300,text="赤の勝ち",fill='black',font=('Helvetica', 60))
            over = True
            break
        if judge() == 2:
            cvs.create_text(350,300,text="黄の勝ち",fill='black',font=('Helvetica', 60))
            over = True
            break

root = tkinter.Tk()
root.title('4目並べ')
root.geometry('700x600')
root.bind('<Button>',pressed)
cvs = tkinter.Canvas(root,width=700,height=600,bg='gray')
cvs.pack()
for i in range(42):
    x = i%7*100
    y = i//7*100
    en = Circle(x,y)
    en.id = cvs.create_oval(x,y,x+100,y+100,fill='white')
    en.stat = 0 #0:白,1:赤,2:黄
    masu.append(en)

root.mainloop()