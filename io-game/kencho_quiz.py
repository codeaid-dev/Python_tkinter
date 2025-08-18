import tkinter, csv, random

FONT = ('sans-serif',16)

def judge():
    answer = answer_entry.get()
    if answer == questions[question]:
        result_label['text'] = '正解！！'
    else:
        result_label['text'] = f'不正解（正解：{questions[question]}）'

def next():
    global question
    question = random.choice(list(questions))
    question_label2['text'] = f'{question}の県庁所在地は？'

with open('kencho.csv', 'r') as f:
    data = csv.reader(f)
    ques, ans = [row for row in data]
questions = dict(zip(ques,ans))
question = random.choice(list(questions))

root = tkinter.Tk()
root.title("県庁所在地クイズ")
root.geometry('500x300')

frame = tkinter.Frame(root)
frame.pack(pady=10)
question_label1 = tkinter.Label(frame, text='問題: ', font=FONT)
question_label1.grid(row=0, column=0)
question_label2 = tkinter.Label(frame, text=f'{question}の県庁所在地は？', font=FONT)
question_label2.grid(row=0, column=1)
answer_label = tkinter.Label(frame, text='答え: ', font=FONT)
answer_label.grid(row=1, column=0)
answer_entry = tkinter.Entry(frame, width=10, font=FONT)
answer_entry.grid(row=1, column=1)

answer_button = tkinter.Button(root, text='解答', font=FONT, command=judge)
answer_button.pack(pady=10)

another_button = tkinter.Button(root, text='別の問題', font=FONT, command=next)
another_button.pack(pady=10)

result_label = tkinter.Label(root, text='ここに結果を表示', font=FONT)
result_label.pack(pady=10)

root.mainloop()
