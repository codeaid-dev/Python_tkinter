import tkinter, random

FONT = ('sans-serif',16)
level = 0
number = None

def start():
    global level, number
    level = 1
    number = str(random.randint(0,9))
    num_label1.config(text=f'{level}桁の数字を覚えてください')
    num_label2.config(text=number)
    num_entry1.delete(0, tkinter.END)
    num_entry1.config(state='disabled')
    answer_button.config(state='disabled')
    result_label.config(fg=default_color)
    result_label.config(text='ここに結果を表示')
    root.after(3000, enable_answer)

def judge():
    global level, number
    ans = num_entry1.get()
    if ans == number:
        result_label.config(text='正解！次のレベルへ進みます。')
        level += 1
        number += str(random.randint(0,9))
        num_label1.config(text=f'{level}桁の数字を覚えてください')
        num_label2.config(text=number)
        num_entry1.delete(0, tkinter.END)
        num_entry1.config(state='disabled')
        answer_button.config(state='disabled')
        root.after(3000, enable_answer)
    else:
        result_label.config(fg='red')
        result_label.config(text=f'間違い！(正解：{number})あなたのレベル：{level-1}')

def enable_answer():
    num_entry1.config(state='normal')
    answer_button.config(state='normal')
    num_label2.config(text='')

root = tkinter.Tk()
root.title("数当て")
root.geometry('600x300')

num_label1 = tkinter.Label(root, text='数字記憶を開始します！', font=FONT)
default_color = num_label1.cget('fg')
num_label1.pack(pady=10)
num_label2 = tkinter.Label(root, text='', font=FONT)
num_label2.pack(pady=10)
frame = tkinter.Frame(root)
frame.pack(pady=10)
num_entry1 = tkinter.Entry(frame, width=15, font=FONT)
num_entry1.grid(row=0, column=0)
answer_button = tkinter.Button(frame, text='解答', font=FONT, command=judge)
answer_button.grid(row=0, column=1)
result_label = tkinter.Label(root, text='ここに結果を表示', font=FONT)
result_label.pack(pady=10)
start_button = tkinter.Button(root, text='スタート・リセット', font=FONT, command=start)
start_button.pack(pady=10)

root.mainloop()
