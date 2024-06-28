import tkinter
import os, json

FONT = ('Helvetica',18)

json_path = os.path.dirname(__file__) + '/sample.json'

def load_json():
    if os.path.exists(json_path):
        with open(json_path, 'rt', encoding='utf-8') as fp:
            try:
                return json.load(fp)
            except Exception:
                return []
    return []

def save_json(data):
    latest = load_json()
    for exist in latest:
        if data['id'] in exist.values():
            return False
    latest.append(data)
    with open(json_path, 'wt', encoding='utf-8') as fp:
        json.dump(latest, fp, ensure_ascii=False, indent=2)

root = tkinter.Tk()
root.title('JSON読み書き')
root.geometry('400x400')

def read():
    data = load_json()
    text.delete("1.0", tkinter.END)
    text.insert("1.0", str(data))

def save():
    data = {}
    data['id'] = id.get()
    data['email'] = email.get()
    data['name'] = name.get()
    data['subject'] = subject.get()
    save_json(data)
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

root.mainloop()