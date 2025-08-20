import tkinter, random

FONT = ('sans-serif',32)
FONT2 = ('sans-serif',20)

def create():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{};:,.<>?'
    d = digit_entry.get()
    if d.isdigit() and 8<=int(d)<=32:
        d = int(d)
        char = random.choice(lower)
        char += random.choice(upper)
        char += random.choice(numbers)
        char += random.choice(symbols)
        password = char
        for i in range(d-len(char)):
            password += random.choice(lower+upper+numbers+symbols)
        password = ''.join(random.sample(password, len(password)))
        result_label['text'] = password
        result_label['fg'] = default_color
    else:
        result_label['text'] = '桁数は8~32の整数を入力してください。'
        result_label['fg'] = 'red'

root = tkinter.Tk()
root.title('パスワード生成')
root.geometry('600x300')

frame = tkinter.Frame(root)
frame.pack(pady=5)

digit_label = tkinter.Label(frame, text='桁数',font=FONT)
digit_label.grid(row=0, column=0)
digit_entry = tkinter.Entry(frame, width=10, font=FONT)
digit_entry.grid(row=0, column=1)

btn = tkinter.Button(root, text='生成', font=FONT, command=create)
btn.pack(pady=5)

result_label = tkinter.Label(root, text='ここに表示',font=FONT2)
default_color = result_label.cget('fg')
result_label.pack(pady=20)

root.mainloop()