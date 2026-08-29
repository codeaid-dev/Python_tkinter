import tkinter

class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.stat = 0 #0:白,1:赤,2:黄

def judge(i):
    player = ens[i].stat
    if player == 0:
        return 0
    row = i // 7
    col = i % 7
    directions = [
        (1, 0),    # 右
        (0, 1),    # 下
        (1, 1),    # 右下
        (1, -1)    # 右上
    ]
    for dx, dy in directions:
        count = 1
        # 正方向を調べる
        for n in range(1, 4):
            x = col + dx * n
            y = row + dy * n
            if 0 <= x < 7 and 0 <= y < 6:
                index = y * 7 + x
                if ens[index].stat == player:
                    count += 1
                else:
                    break
            else:
                break
        # 逆方向を調べる
        for n in range(1, 4):
            x = col - dx * n
            y = row - dy * n
            if 0 <= x < 7 and 0 <= y < 6:
                index = y * 7 + x
                if ens[index].stat == player:
                    count += 1
                else:
                    break
            else:
                break
        if count >= 4:
            return player
    return 0

KAZU = 42
over = False
turn = False # True:赤,False:黄
ens = []
def pressed(event):
    global turn,over
    if over:
        return
    for i,en in enumerate(ens):
        if en.x < event.x < en.x+100 and en.y < event.y < en.y+100:
            if (i>=35 and en.stat==0) or (i<35 and ens[i+7].stat!=0 and en.stat==0):
                if turn:
                  cvs.itemconfig(en.id,fill='red')
                  turn = False
                  en.stat = 1
                else:
                  cvs.itemconfig(en.id,fill='yellow')
                  turn = True
                  en.stat = 2
                # 今置いたコマを起点に判定
                winner = judge(i)
                if winner == 1:
                    cvs.create_text(350,300,text="赤の勝ち",fill='black',font=('Helvetica', 60))
                    over = True
                elif winner == 2:
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
    ens.append(en)

root.mainloop()