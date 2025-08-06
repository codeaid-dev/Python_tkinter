import tkinter,math

root = tkinter.Tk()
root.title('多角形を描画')
cvs = tkinter.Canvas(root,width=300,height=300,bg='white')
cvs.pack()

radius = 100
for i in range(5):
    x = 150 + radius * math.cos(i * 2 * math.pi / 5)
    y = 150 + radius * math.sin(i * 2 * math.pi / 5)
    cvs.create_oval(x-5,y-5,x+5,y+5,fill='black',width=0)
root.mainloop()