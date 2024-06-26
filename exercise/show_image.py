import tkinter

root = tkinter.Tk()
root.title('画像表示')
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
img1 = tkinter.PhotoImage(file='./images/panda.png')
cvs.create_image(250,250,image=img1)
img2 = tkinter.PhotoImage(file='./images/panda_illust.png')
label = tkinter.Label(root, image=img2)
label.pack()

root.mainloop()