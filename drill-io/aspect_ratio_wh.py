import tkinter

FONT = ('sans-serif',16)

def click_radio():
    radio = iv.get()
    if radio == 1:
        height_entry.config(state='readonly')
        width_entry.config(state='normal')
    else:
        height_entry.config(state='normal')
        width_entry.config(state='readonly')

def calc():
    ratio = ratio_entry.get().split(':')
    if len(ratio) != 2:
        result_label.config(foreground='red',background=root.cget('bg'))
        result_label['text'] = '有効なアスペクト比を入力してください。'
        result_label.update()
        return
    try:
        w_ratio = int(ratio[0])
        h_ratio = int(ratio[1])
    except ValueError:
        result_label.config(foreground='red',background=root.cget('bg'))
        result_label['text'] = 'アスペクト比は整数で入力してください。'
        result_label.update()

    if iv.get() == 1:
        # 高さを算出
        try:
            width = int(width_entry.get())
        except ValueError:
            result_label.config(foreground='red',background=root.cget('bg'))
            result_label['text'] = '幅に有効な整数を入力してください。'
            result_label.update()
            return
        height = int(width * (h_ratio / w_ratio))
        height_sv.set(height)
        # height_entry.config(state='normal')
        # height_entry.delete(0, tkinter.END)
        # height_entry.insert(0, height)
        # height_entry.config(state='readonly')
    else:
        # 幅を算出
        try:
            height = int(height_entry.get())
        except ValueError:
            result_label.config(foreground='red',background=root.cget('bg'))
            result_label['text'] = '高さに有効な整数を入力してください。'
            result_label.update()
            return
        width = int(height * (w_ratio / h_ratio))
        width_sv.set(width)
        # width_entry.config(state='normal')
        # width_entry.delete(0, tkinter.END)
        # width_entry.insert(0, width)
        # width_entry.config(state='readonly')

root = tkinter.Tk()
root.title("アスペクト比")
root.geometry('400x250')

frame1 = tkinter.Frame(root)
frame1.pack(pady=10)
aspect_label = tkinter.Label(frame1, text='アスペクト比: ', font=FONT)
aspect_label.grid(row=0, column=0)
ratio_entry = tkinter.Entry(frame1, width=7, font=FONT)
ratio_entry.grid(row=0, column=1)

frame2 = tkinter.Frame(root)
frame2.pack(pady=10)
iv = tkinter.IntVar()
iv.set(1)
width_radio = tkinter.Radiobutton(frame2, text='幅: ', value=1, variable=iv, command=click_radio, font=FONT)
width_radio.grid(row=0, column=0)
width_sv = tkinter.StringVar()
width_entry = tkinter.Entry(frame2, width=7, font=FONT, textvariable=width_sv)
# width_entry = tkinter.Entry(frame2, width=7, font=FONT)
width_entry.grid(row=0, column=1)
height_radio = tkinter.Radiobutton(frame2, text='高さ: ', value=2, variable=iv, command=click_radio, font=FONT)
height_radio.grid(row=0, column=2)
height_sv = tkinter.StringVar()
height_entry = tkinter.Entry(frame2, width=7, font=FONT, textvariable=height_sv)
# height_entry = tkinter.Entry(frame2, width=7, font=FONT)
height_entry.config(state='disabled')
height_entry.grid(row=0, column=3)

calc_button = tkinter.Button(root, text='計算', font=FONT, command=calc)
calc_button.pack(pady=10)

result_label = tkinter.Label(root, text='ここにエラーを表示', font=FONT)
result_label.pack(pady=10)

root.mainloop()
