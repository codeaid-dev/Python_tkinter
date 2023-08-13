import tkinter

def file_open():
    cvs.delete('all')
    cvs.create_text(250,100,text="ファイルを開く",fill='black',font=('メイリオ',20))

def file_save():
    cvs.delete('all')
    cvs.create_text(250,100,text="ファイルを保存",fill='black',font=('メイリオ',20))

def displayed():
    cvs.delete('all')
    cvs.create_text(250,100,text=f"表示1:{bv1.get()}, 表示2:{bv2.get()}, 表示3:{bv3.get()}",fill='black',font=('メイリオ',20))

def selected():
    cvs.delete('all')
    cvs.create_text(250,100,text=f"{iv.get()}を選択",fill='black',font=('メイリオ',20))

root = tkinter.Tk()
root.title('コマンドメニュー')
cvs = tkinter.Canvas(width=500, height=200, bg='white')
cvs.pack()

menu = tkinter.Menu(root)
menu_file = tkinter.Menu(menu,tearoff=0)
menu_file.add_command(label='開く',command=file_open)
menu_file.add_command(label='保存',command=file_save)
menu_file.add_separator()
menu_file.add_command(label='終了',command=root.destroy)

menu_display = tkinter.Menu(menu,tearoff=0)
bv1 = tkinter.BooleanVar()
bv2 = tkinter.BooleanVar()
bv3 = tkinter.BooleanVar()
menu_display.add_checkbutton(label='表示1',variable=bv1,command=displayed)
menu_display.add_checkbutton(label='表示2',variable=bv2,command=displayed)
menu_display.add_checkbutton(label='表示3',variable=bv3,command=displayed)

iv = tkinter.IntVar()
menu_select = tkinter.Menu(menu,tearoff=0)
menu_select.add_radiobutton(label='選択1',variable=iv,value=1,command=selected)
menu_select.add_radiobutton(label='選択2',variable=iv,value=2,command=selected)
menu_select.add_radiobutton(label='選択3',variable=iv,value=3,command=selected)

menu.add_cascade(label='ファイル',menu=menu_file)
menu.add_cascade(label='表示',menu=menu_display)
menu.add_cascade(label='選択',menu=menu_select)

root.config(menu=menu)
root.mainloop()