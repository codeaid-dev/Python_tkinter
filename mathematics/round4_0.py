import tkinter,math

rw, rh = 100, 200 # rw:横半径、rh:縦半径
centerX, centerY = 250, 250
def main():
    cvs.delete('circle')
    for i in range(0, 360, 10):
        rad = i * math.pi/180
        x = centerX+rw*math.cos(rad)
        y = centerY+rh*math.sin(rad)
        cvs.create_oval(x-2.5,y-2.5,
                        x+2.5,y+2.5,
                        fill='black',
                        width=0,tags='circle')
    root.after(17,main)

root = tkinter.Tk()
root.title('楕円の円周上の座標')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

main()
root.mainloop()