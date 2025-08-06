import tkinter,math

radius=125
angle=0
def main():
    global angle
    angle += 0.1
    x = 250+radius*math.cos(math.radians(angle))
    y = 250+radius*math.sin(math.radians(angle))
    cvs.create_oval(x-2.5,y-2.5,x+2.5,y+2.5,
                    fill='white',width=0,tags='circle')
    x = x+radius*math.cos(math.radians(angle)*36)
    y = y+radius*math.sin(math.radians(angle)*36)
    cvs.create_oval(x-2.5,y-2.5,x+2.5,y+2.5,
                    fill='red',width=0,tags='circle')
    root.after(17,main)

root = tkinter.Tk()
root.title('幾何学模様')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='black')
cvs.pack()

main()
root.mainloop()