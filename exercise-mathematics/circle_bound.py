import tkinter,math,random

dir=random.randint(0,360)
x,y=250,250
speed=5
def main():
    global x,y,dir
    cvs.delete('circle')
    x += speed * math.cos(math.radians(dir))
    y += speed * math.sin(math.radians(dir))
    cvs.create_oval(x-15,y-15,x+15,y+15,
                    fill='black',width=0,
                    tags='circle')
    if x < 15 or x > 485:
        dir = 180-dir
    if y < 15 or y > 485:
        dir *= -1
    root.after(17,main)

root = tkinter.Tk()
root.title('円がウロウロする')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

main()
root.mainloop()