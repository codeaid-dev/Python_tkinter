import tkinter

FONT = ('sans-serif',16)
genotype = ['AA','AO','BB','BO','AB','OO']

def blood_type():
    mom = mother_sv.get()
    dad = father_sv.get()
    child = []
    for m in mom:
        for d in dad:
            child.append(f'{m}{d}')
    blood = []
    for ch in child:
        if ch == 'AA' or ch == 'AO' or ch == 'OA':
            blood.append('A型')
        elif ch == 'BB' or ch == 'BO' or ch == 'OB':
            blood.append('B型')
        elif ch == 'OO':
            blood.append('O型')
        else:
            blood.append('AB型')
    msg = 'と'.join(set(blood))
    msg = '子の血液型は'+msg+'の可能性があります。'
    result_label['text'] = msg

root = tkinter.Tk()
root.title("血液型")
root.geometry('600x200')

frame = tkinter.Frame(root)
frame.pack(pady=10)

mother_sv = tkinter.StringVar()
mother_sv.set(genotype[0])
mother_label = tkinter.Label(frame, text='母親の遺伝子型: ', font=FONT)
mother_label.grid(row=0, column=0)
mother_menu = tkinter.OptionMenu(frame, mother_sv, *genotype)
# mother_menu.config(font=FONT20)
mother_menu.grid(row=0, column=1)

father_sv = tkinter.StringVar()
father_sv.set(genotype[0])
father_label = tkinter.Label(frame, text='父親の遺伝子型: ', font=FONT)
father_label.grid(row=0, column=2)
father_menu = tkinter.OptionMenu(frame, father_sv, *genotype)
# father_menu.config(font=FONT20)
father_menu.grid(row=0, column=3)

button = tkinter.Button(root, text='表示',
                      command=blood_type,
                      width=2,
                      font=FONT)
button.pack(pady=10)
result_label = tkinter.Label(root, text='ここに結果を表示', font=FONT)
result_label.pack(pady=10)

root.mainloop()
