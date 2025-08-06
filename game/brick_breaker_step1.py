import tkinter

class Brick:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

keys = set()
def key_down(e):
    keys.add(e.keysym)
def key_up(e):
    keys.discard(e.keysym)

def main():
    if 'Left' in keys:
        cvs.move(bar.id,-5,0)
        bar.x -= 5
    if 'Right' in keys:
        cvs.move(bar.id,5,0)
        bar.x += 5

    root.after(10, main)

root = tkinter.Tk()
root.title('ブロック崩し')
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
root.geometry('600x800')
cvs = tkinter.Canvas(root,width=600,height=800,bg='black')
cvs.pack()

bar = Brick(275,780,50,10)
bar.id = cvs.create_rectangle(bar.x,bar.y,
                              bar.x+bar.w,bar.y+bar.h,
                              fill='white',tags='bar')
main()
root.mainloop()