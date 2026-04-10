import tkinter,math,time

centerX, centerY = 250, 250
hr, mr, sr = 150, 200, 200
def main():
    cvs.delete('clock')
    s = time.localtime().tm_sec
    m = time.localtime().tm_min + (s/60)
    h = time.localtime().tm_hour % 12 + (m/60)
    hdir = h*30-90
    mdir = m*6-90
    sdir = s*6-90
    for i in range(60):
        rad = math.radians(i*6)
        x = centerX+sr*math.cos(rad)
        y = centerY+sr*math.sin(rad)
        if i%5==0:
            id = cvs.create_oval(x-10,y-10,
                                x+10,y+10,
                                fill='red',width=0,
                                tags='clock')
        else:
            id = cvs.create_oval(x-5,y-5,
                                x+5,y+5,
                                fill='gray',
                                width=0,tags='clock')
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