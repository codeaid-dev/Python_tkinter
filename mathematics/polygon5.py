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
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()

p=5
for y in range(3):
    for x in range(3):
        polygon(100+x*150,100+y*150,50,p)
        p+=1
root.mainloop()