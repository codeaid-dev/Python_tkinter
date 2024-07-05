import tkinter,math

def polygon(x,y,radius,num):
    points = []
    for i in range(num):
        px = x + radius * math.cos(i * 2 * math.pi / num)
        py = y + radius * math.sin(i * 2 * math.pi / num)
        points.append((px,py))
    cvs.create_polygon(points,fill='black',width=0)

root = tkinter.Tk()
root.title('多角形を描画')
cvs = tkinter.Canvas(root,width=300,height=300,bg='white')
cvs.pack()

polygon(150,150,100,8)
root.mainloop()