import tkinter, random

flags = ['Belgium','Bulgaria','Denmark','Finland','Germany','Hungary','Italy','Monaco','Poland','Sweden']

def next():
    global correct,img
    correct = random.choice(flags)
    img = tkinter.PhotoImage(file=f'images/{correct}.png')
    question['image'] = img
    question.update()
    result['text'] = 'Result here'

def judge():
    if correct == answer.get():
        result['text'] = 'Correct!'
    else:
        result['text'] = f'Incorrect (It\'s {correct})'
    result.update()

root = tkinter.Tk()
root.title('Flag Quiz')

correct = random.choice(flags)
img = tkinter.PhotoImage(file=f'images/{correct}.png')
question = tkinter.Label(root, image=img)
question.pack(pady=5)

frm = tkinter.Frame(root)
answer = tkinter.StringVar()
answer.set(flags[0])
for i in range(10):
    rb = tkinter.Radiobutton(frm, text=flags[i], value=flags[i], variable=answer, font=('helvetica',20))
    rb.grid(row=i//5, column=i%5)
frm.pack(pady=5)

result = tkinter.Label(root,
            text='Result here',
            fg='orange',
            font=('helvetica', 20))
result.pack(pady=5)

btn1 = tkinter.Button(root,
        text='Answer',
        font=('helvetica', 20),
        command=judge)
btn1.pack(pady=10)
btn2 = tkinter.Button(root,
        text='Next',
        font=('helvetica', 20),
        command=next)
btn2.pack(pady=5)

root.mainloop()