import tkinter

root = tkinter.Tk()
root.title('スロットマシーン')
root.geometry('500x300')

f = tkinter.Frame(root)
f.pack(pady=5)
slot1 = tkinter.Frame(f)
slot1.grid(row=0,column=0)
slot2 = tkinter.Frame(f)
slot2.grid(row=0,column=1)
slot3 = tkinter.Frame(f)
slot3.grid(row=0,column=2)

root.mainloop()