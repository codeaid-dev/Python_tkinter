import tkinter

root = tkinter.Tk()
root.title('円を縦横に並べる')
cvs = tkinter.Canvas(root, width=500, height=500, bg='gray')
cvs.pack()
cnt = 25
size = 500/cnt
for y in range(cnt):
    for x in range(cnt):
        if y//5%2==0:
            if x//5%2==0:
                color = 'white'
            else:
                color = 'black'
        else:
            if x//5%2==1:
                color = 'white'
            else:
                color = 'black'
        cvs.create_oval(x*size,y*size,x*size+size,y*size+size,fill=color,width=0)

root.mainloop()