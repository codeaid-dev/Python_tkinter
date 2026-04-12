import tkinter as tk

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
]
NewList = [
    'アイテム1',
    'アイテム2',
    'アイテム3',
]

app = tk.Tk()

app.geometry('300x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def change():
    menu = tk.Menu(opt)
    for option in NewList:
        menu.add_command(label=option, command=tk._setit(variable, option))
    opt.config(menu=menu)
    variable.set(NewList[0])

btn = tk.Button(text='更新', command=change)
btn.pack(side='bottom')

def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))

variable.trace_add("write", callback)

app.mainloop()