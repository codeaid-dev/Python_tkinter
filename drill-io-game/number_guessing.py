import tkinter, random, time

FONT = ('sans-serif',16)

def show_result():
    try:
        num1 = int(num_entry1.get())
        num2 = int(num_entry2.get())
        num3 = int(num_entry3.get())
    except ValueError:
        result_label.config(fg='red')
        result_label.config(text='整数を入力してください。')
        return

    if num1 == number1:
        num_label1.config(fg='red')
        num_label1.config(text=str(num1))
    elif num1 > number1:
        num_label1.config(fg=default_color)
        num_label1.config(text='LOW')
    elif num1 < number1:
        num_label1.config(fg=default_color)
        num_label1.config(text='HIGH')

    if num2 == number2:
        num_label2.config(fg='red')
        num_label2.config(text=str(num2))
    elif num2 > number2:
        num_label2.config(fg=default_color)
        num_label2.config(text='LOW')
    elif num2 < number2:
        num_label2.config(fg=default_color)
        num_label2.config(text='HIGH')

    if num3 == number3:
        num_label3.config(fg='red')
        num_label3.config(text=str(num3))
    elif num3 > number3:
        num_label3.config(fg=default_color)
        num_label3.config(text='LOW')
    elif num3 < number3:
        num_label3.config(fg=default_color)
        num_label3.config(text='HIGH')

    if num1 == number1 and num2 == number2 and num3 == number3:
        result_label.config(text=f'経過時間: {time.time()-start:.0f}秒')

def init():
    global number1, number2, number3, start
    number1 = random.randint(1,9)
    number2 = random.randint(1,9)
    number3 = random.randint(1,9)
    num_entry1.delete(0, tkinter.END)
    num_entry2.delete(0, tkinter.END)
    num_entry3.delete(0, tkinter.END)
    num_label1.config(fg=default_color)
    num_label2.config(fg=default_color)
    num_label3.config(fg=default_color)
    num_label1.config(text='?')
    num_label2.config(text='?')
    num_label3.config(text='?')
    result_label.config(fg=default_color)
    result_label.config(text='ここに3つ当てた時間を表示')
    start = time.time()

root = tkinter.Tk()
root.title("数当て")
root.geometry('400x300')

frame = tkinter.Frame(root)
frame.pack(pady=10)
num_label1 = tkinter.Label(frame, text='?', font=FONT)
default_color = num_label1.cget('fg')
num_label1.grid(row=0, column=0)
num_label2 = tkinter.Label(frame, text='?', font=FONT)
num_label2.grid(row=0, column=1)
num_label3 = tkinter.Label(frame, text='?', font=FONT)
num_label3.grid(row=0, column=2)
num_entry1 = tkinter.Entry(frame, width=4, font=FONT)
num_entry1.grid(row=1, column=0)
num_entry2 = tkinter.Entry(frame, width=4, font=FONT)
num_entry2.grid(row=1, column=1)
num_entry3 = tkinter.Entry(frame, width=4, font=FONT)
num_entry3.grid(row=1, column=2)

answer_button = tkinter.Button(root, text='解答', font=FONT, command=show_result)
answer_button.pack(pady=10)

result_label = tkinter.Label(root, text='ここに3つ当てた時間を表示', font=FONT)
result_label.pack(pady=10)

another_button = tkinter.Button(root, text='別の問題', font=FONT, command=init)
another_button.pack(pady=10)

init()
root.mainloop()
