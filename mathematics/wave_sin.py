import tkinter,math

root = tkinter.Tk()
root.title('波を描く')
cvs = tkinter.Canvas(root,width=600,
                     height=500,bg='white')
cvs.pack()
centerY = 250
for x in range(600):
    y = centerY+math.sin(x*0.01)*100
    cvs.create_oval(x-1,y-1,
                    x+1,y+1,
                    fill='black',width=0)

root.mainloop()