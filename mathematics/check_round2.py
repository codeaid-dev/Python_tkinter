import tkinter,math

dir=0
radius=200
def main():
    global dir
    x = 250+radius*math.cos(dir*math.pi/180)
    y = 250+radius*math.sin(dir*math.pi/180)
    cvs.create_oval(x-5,y-5,
                    x+5,y+5,
                    fill='black',
                    width=0,tags='circle')
    dir+=5
    root.after(17,main)

root = tkinter.Tk()
root.title('円周動作')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

main()
root.mainloop()