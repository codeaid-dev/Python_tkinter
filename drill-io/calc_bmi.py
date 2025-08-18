import tkinter

FONT = ('sans-serif',16)

def bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        num = weight / ((height/100)**2)
        if num < 16:
            result = '痩せすぎ'
        elif 16.0 <= num <= 16.99:
            result = '痩せ'
        elif 17.0 <= num <= 18.49:
            result = '痩せぎみ'
        elif 18.50 <= num <= 24.99:
            result = '普通体重'
        elif 25.0 <= num <= 29.99:
            result = '前肥満'
        elif 30.0 <= num <= 34.99:
            result = '肥満(1度)'
        elif 35.0 <= num <= 39.99:
            result = '肥満(2度)'
        else:
            result = '肥満(3度)'
        result_label.config(foreground='black',background='white')
        result_label['text'] = f'BMI値：{num:.2f}　判定：{result}です。'
        result_label.update()
    except ValueError:
        result_label.config(foreground='red',background=root.cget('bg'))
        result_label['text'] = '有効な値を入力してください。'
        result_label.update()

root = tkinter.Tk()
root.title("あなたの星座")
root.geometry('400x200')

frame = tkinter.Frame(root)
frame.pack(pady=10)
height_label = tkinter.Label(frame, text='身長(cm)',font=FONT)
height_label.grid(row=0, column=0)
height_entry = tkinter.Entry(frame, width=7, font=FONT)
height_entry.grid(row=0, column=1)
weight_label = tkinter.Label(frame, text='体重(kg)',font=FONT)
weight_label.grid(row=1, column=0)
weight_entry = tkinter.Entry(frame, width=7, font=FONT)
weight_entry.grid(row=1, column=1)

measurement = tkinter.Button(root, text='測定', font=FONT, command=bmi)
measurement.pack(pady=10)

result_label = tkinter.Label(root, text='ここに表示', font=FONT)
result_label.pack(pady=10)

root.mainloop()
