import tkinter, random

FONT = ('Helvetica',32)
FONT2 = ('Helvetica',20)

def create():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{};:,.<>?'
    d = digit.get()
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
        result['text'] = password
        result['bg'] = 'white'
        result['fg'] = 'black'
    else:
        result['text'] = '桁数は8~32の整数を入力してください。'
        result['bg'] = 'white'
        result['fg'] = 'red'

root = tkinter.Tk()
root.title('パスワード生成')
root.geometry('400x200')

f1 = tkinter.Frame(root)
f1.pack(pady=5)

l1 = tkinter.Label(f1, text='桁数',font=FONT)
l1.grid(row=0, column=0)
digit = tkinter.Entry(f1, width=10, font=FONT)
digit.grid(row=0, column=1)

btn = tkinter.Button(root, text='生成', font=FONT, command=create)
btn.pack(pady=5)

result = tkinter.Label(root, text='ここに表示',font=FONT2)
result.pack(pady=10)

root.mainloop()