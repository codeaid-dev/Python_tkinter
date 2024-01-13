import tkinter

root = tkinter.Tk()
root.title('図形を描画する')

cvs = tkinter.Canvas(root, width=800, height=250)
cvs.pack()
cvs.create_line(50,50,200,200,fill='red',width=5)
cvs.create_rectangle(200,50,300,200,fill='blue',outline='yellow',width=5)
cvs.create_oval(305,50,405,200,fill='green',outline='gold',width=5)
cvs.create_arc(410,50,510,200,fill='yellow',start=45,extent=270,style=tkinter.PIESLICE)
cvs.create_polygon(550,50,500,200,600,200,fill='cyan',outline='gray',width=5)
cvs.create_polygon(630,50,610,200,710,200,690,50,fill='magenta',outline='lime',width=5)

root.mainloop()