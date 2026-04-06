import tkinter

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def normalize(self):
        num = (self.x**2 + self.y**2)**0.5
        self.x = self.x / num
        self.y = self.y / num

Px,Py = 0,0
def motion(e):
    global Px,Py
    Px = e.x
    Py = e.y

cross_x,cross_y = 0,0
def collision(Ax,Ay,Bx,By,Px,Py,radius):
    global cross_x,cross_y
    AP = Vector(Px-Ax,Py-Ay)
    AB = Vector(Bx-Ax,By-Ay)
    AB.normalize()

    #単位ベクトルABとベクトルAPの内積(AXの距離)
    lenAX = AB.x*AP.x+AB.y*AP.y
    if lenAX < 0:
        #AXが負ならAPが最短距離
        shortest = ((Ax-Px)**2 + (Ay-Py)**2)**0.5
    elif lenAX > ((Ax-Bx)**2 + (Ay-By)**2)**0.5:
        #AXがABより長い場合はBPが最短距離
        shortest = ((Bx-Px)**2 + (By-Py)**2)**0.5
    else:
        #単位ベクトルAPとベクトルAPの外積(PXの距離)
        lenPX = AB.x*AP.y-AB.y*AP.x
        #PがAB線分上にあるので、PXが最短距離
        shortest = abs(lenPX)

    cross_x = Ax+(AB.x*lenAX)
    cross_y = Ay+(AB.y*lenAX)

    if shortest < radius:
        return True
    return False

def main():
    cvs.delete('all')
    Ax = 150
    Ay = 350
    Bx = 350
    By = 150
    radius = 50
    hit = False
    cvs.create_line(Ax,Ay,Bx,By,
                    fill='black',width=3)
    if collision(Ax,Ay,Bx,By,Px,Py,radius):
        hit = True
        cvs.create_oval(Px-radius,Py-radius,
                        Px+radius,Py+radius,
                        fill='red',width=0)
    else:
        cvs.create_oval(Px-radius,Py-radius,
                        Px+radius,Py+radius,
                        fill='green',width=0)
    if hit:
        cvs.create_oval(cross_x-5,cross_y-5,
                        cross_x+5,cross_y+5,
                        fill='yellow',width=0)
    root.after(17,main)

root = tkinter.Tk()
root.title('線分と円の当たり判定')
root.bind('<Motion>', motion)
cvs = tkinter.Canvas(root,width=500,
                     height=500,bg='white')
cvs.pack()

main()
root.mainloop()