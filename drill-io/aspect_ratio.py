import tkinter

FONT = ('sans-serif',16)

def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)

def aspect():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        g = gcd(width, height)
        rw = width // g
        rh = height // g
        result_label.config(foreground='black',background='white')
        result_label['text'] = f'{rw}:{rh}'
    except ValueError:
        result_label.config(foreground='red',background=root.cget('bg'))
        result_label['text'] = '有効な値を入力してください。'
        result_label.update()

root = tkinter.Tk()
root.title("アスペクト比")
root.geometry('400x200')

frame = tkinter.Frame(root)
frame.pack(pady=10)
width_label = tkinter.Label(frame, text='幅: ',font=FONT)
width_label.grid(row=0, column=0)
width_entry = tkinter.Entry(frame, width=7, font=FONT)
width_entry.grid(row=0, column=1)
height_label = tkinter.Label(frame, text='高さ: ',font=FONT)
height_label.grid(row=1, column=0)
height_entry = tkinter.Entry(frame, width=7, font=FONT)
height_entry.grid(row=1, column=1)

calc = tkinter.Button(root, text='計算', font=FONT, command=aspect)
calc.pack(pady=10)

result_label = tkinter.Label(root, text='ここに結果を表示', font=FONT)
result_label.pack(pady=10)

root.mainloop()
