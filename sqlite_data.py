import tkinter
import os, sqlite3

FONT = ('メイリオ',18)

db_path = os.path.dirname(__file__) + '/sample.db'

def create_db():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL,
        name TEXT NOT NULL,
        subject TEXT NOT NULL
    )
    ''')
    con.commit()
    con.close()

def submit():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    if id.get() == '':
        cur.execute('INSERT INTO users (email, name, subject) VALUES (:email, :name, :subject)',
                {
                    'email': email.get() or None,
                    'name': name.get() or None,
                    'subject': subject.get() or None
                })
    else:
        cur.execute('INSERT INTO users VALUES (:id, :email, :name, :subject)',
                {
                    'id': id.get() or None,
                    'email': email.get() or None,
                    'name': name.get() or None,
                    'subject': subject.get() or None
                })
    con.commit()
    con.close()

def query():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    result = cur.fetchall()
    con.commit()
    con.close()
    new_list = []
    for id,email,name,subject in result:
        new_dict = {}
        new_dict['id'] = id
        new_dict['email'] = email
        new_dict['name'] = name
        new_dict['subject'] = subject
        new_list.append(new_dict)

    return new_list

root = tkinter.Tk()
root.title('SQLite読み書き')
root.geometry('400x400')

def read():
    data = query()
    text.delete("1.0", tkinter.END)
    text.insert("1.0", str(data))

def save():
    submit()
    id.delete(0, tkinter.END)
    email.delete(0, tkinter.END)
    name.delete(0, tkinter.END)
    subject.delete(0, tkinter.END)

f1 = tkinter.Frame(root)
f1.pack()

l1 = tkinter.Label(f1, text='ID')
l1.grid(row=0, column=0)
l2 = tkinter.Label(f1, text='メールアドレス')
l2.grid(row=1, column=0)
l3 = tkinter.Label(f1, text='名前')
l3.grid(row=2, column=0)
l4 = tkinter.Label(f1, text='学習科目')
l4.grid(row=3, column=0)

id = tkinter.Entry(f1, width=20, font=FONT)
id.grid(row=0, column=1)
email = tkinter.Entry(f1, width=20, font=FONT)
email.grid(row=1, column=1)
name = tkinter.Entry(f1, width=20, font=FONT)
name.grid(row=2, column=1)
subject = tkinter.Entry(f1, width=20, font=FONT)
subject.grid(row=3, column=1)

f2 = tkinter.Frame(root)
f2.pack()

btn1 = tkinter.Button(f2, text='読み込む', font=FONT, command=read)
btn1.pack(side=tkinter.LEFT, padx=10)
btn2 = tkinter.Button(f2, text='書き込む', font=FONT, command=save)
btn2.pack(side=tkinter.LEFT, padx=10)

text = tkinter.Text(root, width=50, height=10)
text.pack()

create_db()
root.mainloop()