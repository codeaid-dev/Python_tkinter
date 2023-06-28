import tkinter

root = tkinter.Tk()
root.title('市松模様')
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
for y in range(10):
    for x in range(10):
        if (x%2==0 and y%2==0) or (x%2==1 and y%2==1):
            cvs.create_rectangle(x*50,y*50,x*50+50,y*50+50,fill='white',width=0)
        else:
            cvs.create_rectangle(x*50,y*50,x*50+50,y*50+50,fill='black',width=0)

root.mainloop()
