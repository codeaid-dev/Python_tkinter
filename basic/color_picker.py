import tkinter
from tkinter import colorchooser

root=tkinter.Tk()
root.title('Color Picker')
root.geometry('400x400')

def color():
    color = colorchooser.askcolor()
    label = tkinter.Label(root,
            text=f'R:{color[0][0]} G:{color[0][1]} B:{color[0][2]} {color[1]}',
            font=('Helvetica',32),
            bg=color[1],
            fg='black').pack(pady=10)

button = tkinter.Button(root, text='色選択', command=color).pack()

root.mainloop()