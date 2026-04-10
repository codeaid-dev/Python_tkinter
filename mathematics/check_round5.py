import tkinter,math

dir=0
radius=200
def main():
    global dir
    cvs.delete('circle')
    # x = 250+radius*math.cos(dir*3*math.pi/180)
    y = 250+radius*math.sin(dir*4*math.pi/180)
    cvs.create_oval(dir-10,y-10,
                    dir+10,y+10,
                    fill='black',
                    width=0,tags='circle')
    dir+=1
    if dir>500: dir = 0
    root.after(17,main)

root = tkinter.Tk()
root.title('円周動作')
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

main()
root.mainloop()