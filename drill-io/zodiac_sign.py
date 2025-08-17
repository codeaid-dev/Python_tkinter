import tkinter

FONT20 = ('sans-serif',20)
seiza = ['山羊座','水瓶座','魚座','牡羊座','牡牛座','双子座','蟹座','獅子座','乙女座','天秤座','蠍座','射手座']
end_date = [19,18,20,19,20,21,22,22,22,23,22,21]
month = [i for i in range(1,13)]
date = [i for i in range(1,32)]

def zodiac():
    m = month_iv.get()
    d = date_iv.get()
    if m == 2 and d >=29:
        d = 29
    elif m in [4,6,9,11] and d >= 31:
        d = 30

    if end_date[m-1] >= d:
        msg = f'{m}月{d}日は{seiza[m-1]}です'
    else:
        msg = f'{m}月{d}日は{seiza[m%12]}です'

    result['text'] = msg

root = tkinter.Tk()
root.title("あなたの星座")
root.geometry('400x200')

frame = tkinter.Frame(root)
frame.pack(pady=10)

month_iv = tkinter.IntVar()
month_iv.set(month[0])
month_menu = tkinter.OptionMenu(frame, month_iv, *month)
month_menu.grid(row=0, column=0)
month_label = tkinter.Label(frame, text='月')
month_label.grid(row=0, column=1)

date_iv = tkinter.IntVar()
date_iv.set(date[0])
month_menu = tkinter.OptionMenu(frame, date_iv, *date)
month_menu.grid(row=0, column=2)
date_label = tkinter.Label(frame, text='日')
date_label.grid(row=0, column=3)

button = tkinter.Button(root, text='表示',
                      command=zodiac,
                      width=2,
                      font=FONT20)
button.pack(pady=10)
result = tkinter.Label(root, text='ここに表示', font=FONT20)
result.pack(pady=10)

root.mainloop()
