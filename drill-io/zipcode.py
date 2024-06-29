import tkinter, csv

FONT = ('Helvetica',16)

def ziptoadd():
    z1 = zip1.get()
    z2 = zip2.get()
    z2 = z2 if z2 != '' else '0000'
    for z in zips:
        if z['zipcode'] == z1+z2:
            add1.delete(0,tkinter.END)
            add1.insert(tkinter.END,z['city'])
            add = z['place'] if z['place'] != '以下に掲載がない場合' else ''
            add2.delete(0,tkinter.END)
            add2.insert(tkinter.END,add)
            break

def addtozip():
    city = add1.get()
    place = add2.get()
    for z in zips:
        if z['city'] == city and (z['place'] == place or place == ''):
            zip1.delete(0,tkinter.END)
            zip1.insert(tkinter.END,z['zipcode'][:3])
            zip2.delete(0,tkinter.END)
            zip2.insert(tkinter.END,z['zipcode'][3:])
            break

zips = []
with open('27OSAKA.csv', 'r', encoding='shift-jis') as f:
    data = csv.reader(f)
    for row in data:
        zip = {}
        zip['zipcode'] = row[2]
        zip['city'] = row[7]
        zip['place'] = row[8]
        zips.append(zip)

root = tkinter.Tk()
root.title('大阪府-郵便番号検索')
root.geometry('600x200')

f1 = tkinter.Frame(root)
f1.pack(pady=5)
l1 = tkinter.Label(f1, text='郵便番号',font=FONT)
l1.grid(row=0, column=0)
zip1 = tkinter.Entry(f1, width=3, font=FONT)
zip1.grid(row=0, column=1)
l2 = tkinter.Label(f1, text='-',font=FONT)
l2.grid(row=0, column=2)
zip2 = tkinter.Entry(f1, width=4, font=FONT)
zip2.grid(row=0, column=3)
btn1 = tkinter.Button(f1, text='検索', font=FONT, command=ziptoadd)
btn1.grid(row=0, column=4)

l3 = tkinter.Label(root, text='----------',font=FONT)
l3.pack(pady=10)

f2 = tkinter.Frame(root)
f2.pack(pady=5)
l4 = tkinter.Label(f2, text='市町村名',font=FONT)
l4.grid(row=0, column=0)
add1 = tkinter.Entry(f2, width=30, font=FONT)
add1.grid(row=0, column=1)
l4 = tkinter.Label(f2, text='地名',font=FONT)
l4.grid(row=1, column=0)
add2 = tkinter.Entry(f2, width=30, font=FONT)
add2.grid(row=1, column=1)
btn2 = tkinter.Button(f2, text='検索', font=FONT, command=addtozip)
btn2.grid(row=1, column=2)

root.mainloop()