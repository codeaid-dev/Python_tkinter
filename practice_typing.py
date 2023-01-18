import tkinter
import random, time

alphabet = 'abcdefghijklmnopqrstuvwxyz'
target = ''
start = None
count, clear = 0, 0
over = False

def key(e):
    global target, start, clear, count, over
    if over:
        return
    if len(target) == 0:
        target = random.choice(alphabet)
        ques['text'] = target
        ans['text'] = ''
        start = time.time()
        return

    ans['text'] = e.keysym
    ans.update()
    if target == e.keysym:
        clear += 1
        ques['fg'] = 'cyan'
        ques.update()
    else:
        ques['fg'] = 'red'
        ques.update()
    count += 1
    time.sleep(0.1)
    ques['fg'] = 'black'
    ques.update()
    target = random.choice(alphabet)
    ques['text'] = target
    ques.update()
    ans['text'] = ''
    ans.update()

    if time.time() - start > 10:
        res['text'] = f'clear {clear} in {count}({int(clear/count*100)}%)'
        res.update()
        over = True

root = tkinter.Tk()
root.title('タイピング練習')
root.geometry('400x200')
root['bg'] = 'white'
root.bind('<Key>', key)
ques = tkinter.Label(root,text='Start <Press any key>',font=('Helvetica',32),fg='black',bg='white')
ques.pack(pady=10)
ans = tkinter.Label(root,text='Answer here',font=('Helvetica',32),fg='black',bg='white')
ans.pack(pady=10)
res = tkinter.Label(root,text='Result here',font=('Helvetica',32),fg='black',bg='white')
res.pack()

root.mainloop()