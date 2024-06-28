import tkinter
import os, json

FONT = ('Helvetica',18)
ISBN_CHAR = '0123456789-'

json_path = os.path.dirname(__file__) + '/books.json'

def load_json():
    if os.path.exists(json_path):
        with open(json_path, 'rt', encoding='utf-8') as fp:
            try:
                return json.load(fp)
            except Exception:
                print('error')
                return []
    return []

def save_json(data):
    info['fg'] = 'red'
    if data['name']=='' or data['isbn']=='' or data['price']=='':
        info['text'] = '項目はすべて入力してください。'
        return False
    if not data['price'].isdecimal():
        info['text'] = '価格は数字で入力してください。'
        return False
    for s in data['isbn']:
        if s not in ISBN_CHAR:
            info['text'] = 'ISBNに数字とハイフン以外が含まれています。'
            return False
    data['isbn'] = data['isbn'].replace('-','')
    latest = load_json()
    for exist in latest:
        for s in exist.values():
            if s == data['isbn']:
                info['text'] = 'ISBNがすでにあります。'
                return False
    latest.append(data)
    with open(json_path, 'wt', encoding='utf-8') as fp:
        json.dump(latest, fp, ensure_ascii=False, indent=2)
    info['fg'] = 'green'
    info['text'] = '書き込みました。'
    return True

root = tkinter.Tk()
root.title('書籍価格帳')
root.geometry('400x400')

def read():
    data = load_json()
    text.delete("1.0", tkinter.END)
    books = ''
    for book in data:
        books += f"書籍名：{book['name']}\nISBN：{book['isbn']}\n価格：{book['price']}円\n"
        books += '==========\n'
    text.insert("1.0", books)
    info['fg'] = 'green'
    info['text'] = '読み込みました。'

def save():
    data = {}
    data['name'] = name.get()
    data['isbn'] = isbn.get()
    data['price'] = price.get()
    if save_json(data):
        name.delete(0, tkinter.END)
        isbn.delete(0, tkinter.END)
        price.delete(0, tkinter.END)

def remove():
    info['fg'] = 'red'
    if isbn.get() == '':
        info['text'] = 'ISBNを入力してください。'
        return
    for s in isbn.get():
        if s not in ISBN_CHAR:
            info['text'] = 'ISBNに数字とハイフン以外が含まれています。'
            return
    data = load_json()
    latest = []
    for book in data:
        if isbn.get().replace('-','') != book['isbn']:
            latest.append(book)

    with open(json_path, 'wt', encoding='utf-8') as fp:
        json.dump(latest, fp, ensure_ascii=False, indent=2)

    isbn.delete(0, tkinter.END)
    info['fg'] = 'green'
    info['text'] = '削除しました。'


f1 = tkinter.Frame(root)
f1.pack(pady=5)

l1 = tkinter.Label(f1, text='書籍名')
l1.grid(row=0, column=0)
l2 = tkinter.Label(f1, text='ISBN')
l2.grid(row=1, column=0)
l3 = tkinter.Label(f1, text='価格')
l3.grid(row=2, column=0)

name = tkinter.Entry(f1, width=20, font=FONT)
name.grid(row=0, column=1)
isbn = tkinter.Entry(f1, width=20, font=FONT)
isbn.grid(row=1, column=1)
price = tkinter.Entry(f1, width=20, font=FONT)
price.grid(row=2, column=1)

f2 = tkinter.Frame(root)
f2.pack(pady=5)

info = tkinter.Label(root, text='')
info.pack(pady=5)

btn1 = tkinter.Button(f2, text='読み込む', font=FONT, command=read)
btn1.pack(side=tkinter.LEFT, padx=10)
btn2 = tkinter.Button(f2, text='書き込む', font=FONT, command=save)
btn2.pack(side=tkinter.LEFT, padx=10)
btn3 = tkinter.Button(f2, text='削除', font=FONT, command=remove)
btn3.pack(side=tkinter.LEFT, padx=10)

text = tkinter.Text(root, width=50, height=10)
text.pack(pady=5)

root.mainloop()