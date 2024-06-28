import tkinter
import sqlite3, datetime

FONT = ('Helvetica',18)
db_path = 'memo.db'
created, modified = None, None
first_menu = '選択してください'
options = [first_menu]

def create_db():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS memos (
        created TEXT PRIMARY KEY NOT NULL,
        modified TEXT NOT NULL,
        memo TEXT
    )
    ''')
    con.commit()
    con.close()

def submit():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('INSERT INTO memos (created, modified, memo) VALUES (:created, :modified, :memo)',
            {
                'created': created,
                'modified': modified,
                'memo': memo.get(1.0, tkinter.END+'-1c') or None
            })
    con.commit()
    con.close()

def update():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('UPDATE memos SET modified=?, memo=? WHERE created=?', (modified, memo.get(1.0, tkinter.END+'-1c'), created))
    con.commit()
    con.close()

def delete():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('DELETE FROM memos WHERE created=?', (created,))
    con.commit()
    con.close()

def query(item=None):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    if item == None:
        cur.execute('SELECT * FROM memos')
    else:
        cur.execute('SELECT * FROM memos WHERE created=?', (item,))
    result = cur.fetchall()
    con.commit()
    con.close()
    new_list = []
    for created,modified,memo in result:
        new_dict = {}
        new_dict['created'] = created
        new_dict['modified'] = modified
        new_dict['memo'] = memo
        new_list.append(new_dict)

    return new_list

def change_menu(new=None):
    options.clear()
    options.append(first_menu)
    for option in query():
        options.append(option['created'])
    menu = tkinter.Menu(dropdown)
    for option in options:
        menu.add_command(label=option, command=tkinter._setit(selected, option, read))
    dropdown.config(menu=menu)
    if new != None:
        selected.set(new)
    else:
        selected.set(first_menu)

def create():
    global created, modified
    created = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')
    modified = created
    memo.delete(1.0, tkinter.END)
    change_menu()
    lm['text'] = modified

def read(value):
    global created, modified
    memo.delete(1.0, tkinter.END)
    lm['text'] = ''
    if value != first_menu:
        data = query(value)
        memo.insert(1.0, data[0]['memo'])
        created = data[0]['created']
        modified = data[0]['modified']
        lm['text'] = modified

def save():
    global modified
    new = True
    for option in query():
        if created == option['created']:
            new = False
            break
    if new:
        submit()
    else:
        modified = datetime.datetime.now().strftime('%Y年%m月%d日%H:%M:%S')
        lm['text'] = modified
        update()
    change_menu(created)

def remove():
    global created
    memo.delete(1.0, tkinter.END)
    if selected.get() != first_menu:
        created = selected.get()
        delete()
        change_menu()
        lm['text'] = ''

root = tkinter.Tk()
root.title('メモ帳')
root.geometry('500x500')

f1 = tkinter.Frame(root)
f1.pack(pady=10)

l1 = tkinter.Label(f1, text='作成日')
l1.grid(row=0, column=0)
l2 = tkinter.Label(f1, text='編集日')
l2.grid(row=1, column=0)

selected = tkinter.StringVar()
selected.set(options[0])
dropdown = tkinter.OptionMenu(f1, selected, *options, command=read)
dropdown.grid(row=0, column=1)
lm = tkinter.Label(f1, text='')
lm.grid(row=1, column=1)

f2 = tkinter.Frame(root)
f2.pack(pady=10)

memo = tkinter.Text(f2, width=50, height=20)
memo.pack(side=tkinter.LEFT, padx=10)
f3 = tkinter.Frame(root)
f3.pack(pady=10)

btn1 = tkinter.Button(f3, text='新規', font=FONT, command=create)
btn1.pack(side=tkinter.LEFT, padx=10)
btn2 = tkinter.Button(f3, text='保存', font=FONT, command=save)
btn2.pack(side=tkinter.LEFT, padx=10)
btn3 = tkinter.Button(f3, text='削除', font=FONT, command=remove)
btn3.pack(side=tkinter.LEFT, padx=10)

create_db()
change_menu()
root.mainloop()