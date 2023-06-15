import tkinter

class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y

turn = False # True:赤,False:黄
masu = []
def pressed(event):
    global turn
    for i,en in enumerate(masu):
        if en.x < event.x < en.x+100 and en.y < event.y < en.y+100:
            if (i>=35 and en.stat==0) or (masu[i+7].stat!=0 and en.stat==0):
                if turn:
                  cvs.itemconfig(en.id,fill='red')
                  turn = False
                  en.stat = 1
                else:
                  cvs.itemconfig(en.id,fill='yellow')
                  turn = True
                  en.stat = 2

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