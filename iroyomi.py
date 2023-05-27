import tkinter
import random

class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,c):
        self.color = c.upper()
        self.id = cvs.create_oval(self.x-100,self.y-100,self.x+100,self.y+100,fill=self.color,width=0)

def press(e):
    global score
    #print('判定前：',odai)
    for i in range(4):
        dist = (abs(e.x-ens[i].x)**2 + abs(e.y-ens[i].y)**2) ** 0.5
        if dist < 100:
            if odai[2] == 0:
                if odai[0] == i:
                    score += 1
            else:
                if odai[1] == i:
                    score += 1
            odai.clear()
            for i in range(2):
                odai.append(random.randint(0,3))
            odai.append(random.randint(0,1))
            break
    #print('判定後：',odai)

def main():
    global timer,status
    if status == 1:
        cvs.create_text(300,200,fill='black',text='＜終了＞',font=('メイリオ',50,'bold'),tags='gameover')
        return
    cvs.itemconfig('q1',fill=iro[odai[0]],text=moji[odai[1]])
    cvs.itemconfig('q2',text=choice[odai[2]])
    cvs.itemconfig('score',text=f'{score}')
    timer -= 1
    if timer % 100 == 0:
        if timer <= 0:
            cvs.itemconfig('timer',text=f'{timer//100}',fill='red')
            status = 1
        else:
            cvs.itemconfig('timer',text=f'{timer//100}')
    root.after(10, main)

root = tkinter.Tk()
root.title('いろよみ')
root.geometry('600x600')
root.bind('<ButtonPress>',press)
cvs = tkinter.Canvas(root, width=600, height=600, bg='gray')
cvs.pack()
score=0
timer=2000
status=0
iro = ['RED','GREEN','BLUE','YELLOW']
moji = ['赤','緑','青','黄']
choice = ['色','読み']
odai = []
for i in range(2):
    odai.append(random.randint(0,3))
odai.append(random.randint(0,1))
ens = []
ens.append(Circle(300,120))
ens.append(Circle(480,300))
ens.append(Circle(300,480))
ens.append(Circle(120,300))
for i in range(4):
    ens[i].draw(iro[i])

cvs.create_text(300,300,fill=iro[odai[0]],text=moji[odai[1]],font=('メイリオ',40),tags='q1')
cvs.create_text(300,350,fill='black',text=choice[odai[2]],font=('メイリオ',40),tags='q2')
cvs.create_text(60,60,text=f'{score}',fill='black',font=('Times New Roman',50),tags='score')
cvs.create_text(540,60,text=f'{timer//100}',fill='black',font=('Times New Roman',50),tags='timer')
main()
root.mainloop()