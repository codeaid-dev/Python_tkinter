import tkinter
import tkinter.messagebox

labels = []
#True: O, False: X
turn = True
count = 0
def click_label(label):
    if label.widget['state'] == 'disabled':
        return

    global turn, count
    if label.widget['text'] == '' and turn == True:
        label.widget['text'] = 'O'
        turn = False
        count += 1
        check_win()
    elif label.widget['text'] == '' and turn == False:
        label.widget['text'] = 'X'
        turn = True
        count += 1
        check_win()
    else:
        tkinter.messagebox.showerror('Tic-Tac-Toe', 'すでにクリックされています。\n他のマスを選んでください。')

def disable_labels():
    global labels
    for label in labels:
        label['state'] = 'disable'
        #label.config(state='disable')

wins = [[0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]]
winner = 0 # 0:tie, 1:O, 2:X
def check_win():
    global winner
    for i in range(len(wins)):
        a,b,c = wins[i]
        if labels[a]['text'] \
            and labels[a]['text'] == labels[b]['text'] \
            and labels[a]['text'] == labels[c]['text']:
            labels[a].config(bg='red')
            labels[b].config(bg='red')
            labels[c].config(bg='red')
            if labels[a]['text'] == 'O':
                winner = 1
            else:
                winner = 2

    if winner == 1:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Oの勝ちです。')
        disable_labels()
    elif winner == 2:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
        disable_labels()

    if winner == 0 and count == 9:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', '引き分けです。')
        disable_labels()

root = tkinter.Tk()
root.title('Tic-Tac-Toe')

def reset():
    global labels, turn, count, winner
    labels = []
    turn = True
    count = 0
    winner = 0
    for i in range(9):
        label = tkinter.Label(root, text='', font=('Helvetica', 20), height=3, width=6, borderwidth=2, relief='ridge')
        label.grid(row=i//3, column=i%3)
        label.bind('<ButtonPress>', click_label)
        labels.append(label)

my_menu = tkinter.Menu(root)
root.config(menu=my_menu)
options_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='オプション', menu=options_menu)
options_menu.add_command(label='リセット', command=reset)
reset()

root.mainloop()
