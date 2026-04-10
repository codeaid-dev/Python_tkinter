import tkinter,math

mouse = [0]*2
def motion(e):
    mouse[0] = e.x
    mouse[1] = e.y

root = tkinter.Tk()
root.title('波を描く')
root.bind('<Motion>',motion)
cvs = tkinter.Canvas(root,width=600,
                     height=500,bg='white')
cvs.pack()

def main():
    cvs.delete('line')
    centerY = 250
    for x in range(600):
        y = centerY+math.sin((x+mouse[0])*0.01)*mouse[1]
        cvs.create_oval(x-0.25,y-0.25,
                        x+0.25,y+0.25,
                        fill='black',width=0,
                        tags='line')
    root.after(10,main)

main()
root.mainloop()