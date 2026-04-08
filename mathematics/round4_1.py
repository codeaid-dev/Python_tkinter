import tkinter,math

dir=0
rw, rh = 200, 50 # rw:横半径、rh:縦半径
centerX, centerY = 250, 250
def main():
    global dir
    cvs.delete('circle')
    x = centerX+rw*math.cos(dir*math.pi/180)
    y = centerY+rh*math.sin(dir*math.pi/180)
    cvs.create_oval(x-10,y-10,
                    x+10,y+10,
                    fill='cyan',
                    width=0,tags='circle')
    dir+=1
    root.after(17,main)

root = tkinter.Tk()
root.title('地球')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='black')
cvs.pack()

cvs.create_oval(150,150,350,350,
                fill='orange',width=0)
main()
root.mainloop()