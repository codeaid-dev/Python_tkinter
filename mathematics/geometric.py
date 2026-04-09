import tkinter,math

dir=0
radius=125
centerX, centerY = 250, 250
def main():
    global dir
    x = centerX+radius*math.cos(math.radians(dir))
    y = centerY+radius*math.sin(math.radians(dir))
    cvs.create_oval(x-2.5,y-2.5,x+2.5,y+2.5,
                    fill='white',width=0,tags='circle')
    mx = x+radius*math.cos(math.radians(dir)*36)
    my = y+radius*math.sin(math.radians(dir)*36)
    cvs.create_oval(mx-2.5,my-2.5,mx+2.5,my+2.5,
                    fill='red',width=0,tags='circle')
    dir += 0.1
    root.after(17,main)

root = tkinter.Tk()
root.title('幾何学模様')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='black')
cvs.pack()

main()
root.mainloop()