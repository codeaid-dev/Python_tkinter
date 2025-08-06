import tkinter

side = 125
def draw():
    cvs.delete('all')
    for i in range(16):
        x1 = i%4*side
        y1 = i//4*side
        x2 = i%4*side+side
        y2 = i//4*side+side
        cvs.create_rectangle(x1,y1,x2,y2,fill='black',outline='white')

def main():
    draw()
    root.after(200,main)

root = tkinter.Tk()
root.title('神経衰弱')
root.geometry('500x500')

cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()

main()
root.mainloop()
