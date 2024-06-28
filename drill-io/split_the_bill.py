import tkinter

FONT = ('Helvetica',32)
FONT2 = ('Helvetica',20)

def calc():
    t = int(total.get())
    p = int(people.get())
    surplus = (t//p)%100
    num1['text'] = p-1
    num2['text'] = 1
    num3['text'] = p
    if p >= 2 and t >= 200:
        if surplus == 0: #余りがない
            price1['text'] = t // p
            price2['text'] = t // p
        elif iv.get() == 1: #1人が多く払う
            price = t // p
            price1['text'] = (price//100)*100
            price2['text'] = t - price1['text']*(p-1)
        else: #1人が少なく払う
            price = t // p
            price1['text'] = (price//100)*100+100
            price2['text'] = t - price1['text']*(p-1)
        price3['text'] = t

root = tkinter.Tk()
root.title('割り勘計算')
root.geometry('400x400')

f1 = tkinter.Frame(root)
f1.pack(pady=5)

l1 = tkinter.Label(f1, text='支払総額',font=FONT)
l1.grid(row=0, column=0)
l2 = tkinter.Label(f1, text='人数',font=FONT)
l2.grid(row=1, column=0)

total = tkinter.Entry(f1, width=10, font=FONT)
total.grid(row=0, column=1)
people = tkinter.Entry(f1, width=10, font=FONT)
people.grid(row=1, column=1)

l3 = tkinter.Label(root, text='端数処理',font=FONT)
l3.pack(pady=5)

f2 = tkinter.Frame(root)
f2.pack(pady=5)

iv = tkinter.IntVar()
iv.set(1)
txt = ['1人が多く払う','1人が少なく払う']
for i in range(len(txt)):
    r = tkinter.Radiobutton(f2,text=txt[i],value=i+1,variable=iv,font=FONT2)
    r.grid(row=0,column=i)

btn = tkinter.Button(root, text='計算', font=FONT, command=calc)
btn.pack(pady=5)

f3 = tkinter.Frame(root)
f3.pack(pady=5)

l4 = tkinter.Label(f3, text='人数',font=FONT2)
l4.grid(row=0, column=1)
l5 = tkinter.Label(f3, text='支払額(円)',font=FONT2)
l5.grid(row=0, column=2)
l6 = tkinter.Label(f3, text='参加者',font=FONT2)
l6.grid(row=1, column=0)
l7 = tkinter.Label(f3, text='代表',font=FONT2)
l7.grid(row=2, column=0)
l8 = tkinter.Label(f3, text='合計',font=FONT2)
l8.grid(row=3, column=0)
num1 = tkinter.Label(f3, text='-',font=FONT2)
num1.grid(row=1, column=1)
num2 = tkinter.Label(f3, text='-',font=FONT2)
num2.grid(row=2, column=1)
num3 = tkinter.Label(f3, text='-',font=FONT2)
num3.grid(row=3, column=1)
price1 = tkinter.Label(f3, text='-',font=FONT2)
price1.grid(row=1, column=2)
price2 = tkinter.Label(f3, text='-',font=FONT2)
price2.grid(row=2, column=2)
price3 = tkinter.Label(f3, text='-',font=FONT2)
price3.grid(row=3, column=2)

root.mainloop()