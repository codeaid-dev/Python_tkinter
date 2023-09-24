import tkinter
import os, sqlite3

FONT = ('メイリオ',18)

db_path = os.path.dirname(__file__) + '/menu.db'

def create_db():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS menu (
        name TEXT NOT NULL PRIMARY KEY,
        price INT NOT NULL
    )
    ''')
    con.commit()
    con.close()

def submit():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('INSERT INTO menu (name, price) VALUES (:name, :price)',
            {
                'name': name.get() or None,
                'price': price.get() or None
            })
    con.commit()
    con.close()

def query(ryouri=None):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    if ryouri:
        cur.execute('SELECT * FROM menu WHERE name=?', (ryouri,))
    else:
        cur.execute('SELECT * FROM menu')
    result = cur.fetchall()
    con.commit()
    con.close()
    new_list = []
    for name,price in result:
        new_dict = {}
        new_dict['name'] = name
        new_dict['price'] = price
        new_list.append(new_dict)

    return new_list

def delete(ryouri):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('DELETE FROM menu WHERE name=?', (ryouri,))
    con.commit()
    con.close()

def read():
    data = query()
    result = ''
    for item in data:
        result += f"=====\n{item['name']}:{item['price']}円\n"
    text.delete("1.0", tkinter.END)
    text.insert("1.0", result)
    info['fg'] = 'blue'
    info['text'] = '読み込みました。'

def save():
    info['fg'] = 'red'
    if name.get() == '' or price.get() == '':
        info['text'] = '項目はすべて入力してください。'
    elif not price.get().isdigit():
        info['text'] = '価格は整数を入力してください。'
    elif query(name.get()):
        info['text'] = '料理はすでに保存されています。'
    else:
        submit()
        name.delete(0, tkinter.END)
        price.delete(0, tkinter.END)
        info['fg'] = 'blue'
        info['text'] = '保存しました。'

def remove():
    if name.get() == '':
        info['fg'] = 'red'
        info['text'] = '料理名を入力してください。'
    else:
        delete(name.get())
        info['fg'] = 'blue'
        info['text'] = f'{name.get()}を削除しました。'
        name.delete(0, tkinter.END)
        price.delete(0, tkinter.END)

root = tkinter.Tk()
root.title('飲食店メニュー')
root.geometry('400x400')

f1 = tkinter.Frame(root)
f1.pack(pady=5)

l1 = tkinter.Label(f1, text='料理名')
l1.grid(row=0, column=0)
l2 = tkinter.Label(f1, text='価格')
l2.grid(row=1, column=0)

name = tkinter.Entry(f1, width=20, font=FONT)
name.grid(row=0, column=1)
price = tkinter.Entry(f1, width=20, font=FONT)
price.grid(row=1, column=1)

f2 = tkinter.Frame(root)
f2.pack(pady=5)

info = tkinter.Label(root, text='')
info.pack(pady=5)

btn1 = tkinter.Button(f2, text='表示', font=FONT, command=read)
btn1.pack(side=tkinter.LEFT, padx=10)
btn2 = tkinter.Button(f2, text='追加', font=FONT, command=save)
btn2.pack(side=tkinter.LEFT, padx=10)
btn3 = tkinter.Button(f2, text='削除', font=FONT, command=remove)
btn3.pack(side=tkinter.LEFT, padx=10)

text = tkinter.Text(root, width=50, height=13)
text.pack(pady=5)

create_db()
root.mainloop()