import tkinter,math

p=0
radius=200
def main():
    global p
    cvs.delete('circle')
    x = 250+radius*math.cos(p*math.pi/180)
    y = 250+radius*math.sin(p*math.pi/180)
    cvs.create_oval(x-10,y-10,
                    x+10,y+10,
                    fill='cyan',
                    width=0,tags='circle')
    mx = x+30*math.cos(p*12*math.pi/180)
    my = y+30*math.sin(p*12*math.pi/180)
    cvs.create_oval(mx-2.5,my-2.5,
                    mx+2.5,my+2.5,
                    fill='white',
                    width=0,tags='circle')
    p+=0.1
    root.after(17,main)

root = tkinter.Tk()
root.title('地球')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='black')
cvs.pack()

cvs.create_oval(230,230,270,270,
                fill='orange',width=0)
main()
root.mainloop()