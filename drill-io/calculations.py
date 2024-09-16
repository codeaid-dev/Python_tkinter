import tkinter, random

WIDTH,HEIGHT = 400,200
FONT20 = ('Helvetica',20)
FONT50 = ('Helvetica',50)
left,right = 0,0
operator = ''
question = '''表示された数字の結果となる
演算子をクリック
制限時間は60秒!
ここをクリックしてスタート'''
progress = 60
starting = False
correct,incorrect = 0,0

def answer(text):
    def inner():
        if not starting:
            return
        global correct,incorrect,operator
        if (operator == 1 and operations[0] == text) or \
            (operator == 2 and operations[1] == text) or \
            (operator == 3 and operations[2] == text) or \
            (operator == 4 and operations[3] == text):
            correct += 1
        else:
            incorrect += 1
        result['text'] = f'正解数: {correct} 不正解数: {incorrect}'
        make_question()
        labelQ['text'] = question
        labelQ['font'] = FONT50
    return inner

def start(event):
    global starting, progress
    if event.widget == labelQ and not starting:
        progress = 61
        timer()
        starting = True
        make_question()
        labelQ['text'] = question
        labelQ['font'] = FONT50

def timer():
    global progress,starting
    progress -= 1
    labelP['text'] = str(progress)
    if progress <= 0:
        starting = False
        labelP['text'] = 'Time up..'
        return
    root.after(1000, timer)

def make_question():
    global left,right,operator,question
    left = random.randint(1,9)
    right = random.randint(1,9)
    operator = random.randint(1,4)
    if operator == 1: # 足し算
        # 左右とも2で(掛け算と同じになるため)、計算結果が9以下でない間繰り返す
        while (left==2 and right==2) or not (left+right<=9):
            left = random.randint(1,8)
            right = random.randint(1,9-left)
        question = f'{left} ? {right} = {left+right}'
    elif operator == 2: # 引き算
        # 左が4でかつ右が2で(割り算と同じになるため)、計算結果が0~9でない間繰り返す
        while (left==4 and right==2) or not (0<(left-right)<=9):
            left = random.randint(2,8)
            right = random.randint(1,left-1)
        question = f'{left} ? {right} = {left-right}'
    elif operator == 3: # 掛け算
        # 右が1でかつ左右とも2で(足し算と同じになるため)、計算結果が9以下でない間繰り返す
        while right==1 or (left==2 and right==2) or not ((left*right)<=9):
            left = random.randint(1,9)
            right = random.randint(2,9)
        question = f'{left} ? {right} = {left*right}'
    elif operator == 4: # 割り算
        # 右が1でかつ(左が4でかつ右が2)で(引き算と同じになるため)、割り切れない間繰り返す
        while right==1 or (left==4 and right==2) or not (left%right==0):
            left = random.randint(1,9)
            right = random.randint(2,9)
        question = f'{left} ? {right} = {int(left/right)}'

root = tkinter.Tk()
root.title("一桁演算クイズ")
root.geometry('500x350')
root.bind('<Button>', start)
labelP = tkinter.Label(root, text='60', font=FONT50)
labelP.pack(pady=10)
labelQ = tkinter.Label(root, text=question, font=FONT20)
labelQ.pack(pady=10)
operations = ['+','-','×','÷']
operators = tkinter.Frame(root)
operators.pack(pady=10)
btn1 = tkinter.Button(operators, text=operations[0],
                      command=answer(operations[0]),
                      width=2,
                      font=FONT50)
btn1.grid(row=0, column=0)
btn2 = tkinter.Button(operators, text=operations[1],
                      command=answer(operations[1]),
                      width=2,
                      font=FONT50)
btn2.grid(row=0, column=1)
btn3 = tkinter.Button(operators, text=operations[2],
                      command=answer(operations[2]),
                      width=2,
                      font=FONT50)
btn3.grid(row=0, column=2)
btn4 = tkinter.Button(operators, text=operations[3],
                      command=answer(operations[3]),
                      width=2,
                      font=FONT50)
btn4.grid(row=0, column=3)
result = tkinter.Label(root, text=f'正解数: {correct} 不正解数: {incorrect}', font=FONT20)
result.pack(pady=10)

root.mainloop()
