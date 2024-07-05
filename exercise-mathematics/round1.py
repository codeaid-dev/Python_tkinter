import tkinter,math

p=0
radius=200
def main():
    global p
    cvs.delete('circle')
    x = 250+radius*math.cos(p*math.pi/180)
    y = 250+radius*math.sin(p*math.pi/180)
    cvs.create_oval(x-25,y-25,
                    x+25,y+25,
                    fill='cyan',
                    width=0,tags='circle')
    p+=1
    root.after(17,main)

root = tkinter.Tk()
root.title('円周動作')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='black')
cvs.pack()

cvs.create_oval(235,235,265,265,
                fill='orange',width=0)
main()
root.mainloop()