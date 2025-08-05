import tkinter

root = tkinter.Tk()
root.title('ピラミッドのように円を並べる')
cvs = tkinter.Canvas(root, width=500, height=500, bg='white')
cvs.pack()

for row in range(9):
    for col in range(row+1):
        x = (250-(row-col)*25)+col*25
        y = row*50+25
        cvs.create_oval(x-25,y-25,
                        x+25,y+25,
                        fill='black',width=0)

root.mainloop()
