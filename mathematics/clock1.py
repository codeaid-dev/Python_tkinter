import tkinter,math,time

centerX, centerY = 250, 250
hr, mr, sr = 150, 200, 200
def main():
    cvs.delete('clock')
    s = time.localtime().tm_sec
    m = time.localtime().tm_min
    h = time.localtime().tm_hour % 12
    hdir = h*30-90
    mdir = m*6-90
    sdir = s*6-90
    hx = centerX+hr*math.cos(math.radians(hdir))
    hy = centerY+hr*math.sin(math.radians(hdir))
    cvs.create_line(centerX,centerY,
                    hx,hy,
                    fill='black',
                    width=6,tags='clock')
    hx = centerX+mr*math.cos(math.radians(mdir))
    hy = centerY+mr*math.sin(math.radians(mdir))
    cvs.create_line(centerX,centerY,
                    hx,hy,
                    fill='black',
                    width=4,tags='clock')
    hx = centerX+sr*math.cos(math.radians(sdir))
    hy = centerY+sr*math.sin(math.radians(sdir))
    cvs.create_line(centerX,centerY,
                    hx,hy,
                    fill='black',
                    width=2,tags='clock')

    root.after(10,main)

root = tkinter.Tk()
root.title('アナログ時計')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

main()
root.mainloop()