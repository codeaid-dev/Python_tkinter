import tkinter,math

radius=0
def main():
    global radius
    cvs.delete('circle')
    for i in range(0,360,10):
        x = 250+radius*math.cos(i*math.pi/180)
        y = 250+radius*math.sin(i*math.pi/180)
        cvs.create_oval(x-2.5,y-2.5,
                        x+2.5,y+2.5,
                        fill='cyan',
                        width=0,tags='circle')
    radius+=2
    if radius > 200:
        radius = 0
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