import tkinter,math

def star(x,y,radius1,radius2,n):
    angle = (2*math.pi)/(n*2)
    points = []
    for i in range(n*2):
        if i % 2 == 0:
            radius = radius1
        else:
            radius = radius2
#        sx = x+radius*math.cos(i * angle)
#        sy = y+radius*math.sin(i * angle)
        sx = x+radius*math.cos(i * angle - (math.pi/2))
        sy = y+radius*math.sin(i * angle - (math.pi/2))
        points.append((sx,sy))
    cvs.create_polygon(points,
                       fill='yellow',
                       outline='black',
                       width=1)

root = tkinter.Tk()
root.title('n芒星を描画')
cvs = tkinter.Canvas(root,width=300,
                     height=300,bg='white')
cvs.pack()

star(150,150,100,40,5)
root.mainloop()