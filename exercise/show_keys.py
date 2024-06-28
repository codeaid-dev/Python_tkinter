import tkinter

def key(e):
    cvs.delete('all')
    cvs.create_text(200,50,text=f'keycode = {e.keycode}',fill='black',font=('Helvetica',28))
    cvs.create_text(200,150,text=f'keysym = {e.keysym}',fill='black',font=('Helvetica',28))

root = tkinter.Tk()
root.title('キー表示')
root.bind('<Key>', key)
cvs = tkinter.Canvas(root, width=400, height=200, bg='white')
cvs.pack()
cvs.create_text(200,100,text='何かキーを押してください。',fill='black',font=('Helvetica',20))

root.mainloop()