import tkinter

ids = []
colors = ['red','green','blue']
stat = [0 for n in range(25)]

def click(e):
    x = e.x//100
    y = e.y//100
    index = y*5+x
    cvs.itemconfig(ids[index],fill=colors[stat[index]])
    stat[index] = (stat[index]+1) % 3

root = tkinter.Tk()
root.title('クリックして色を変える')
root.geometry('500x500')
root.bind('<Button>',click)
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()

for y in range(5):
    for x in range(5):
        id = cvs.create_rectangle(x*100,y*100,100+x*100,100+y*100,fill='black',outline='white')
        ids.append(id)

root.mainloop()