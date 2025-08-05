import tkinter

class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 0
        self.gravity = 0.05

def main():
    ball.y += ball.speed
    ball.speed += ball.gravity
    if ball.y+100>500:
        # ball.speed *= -0.85
        ball.speed *= -0.98
        ball.y = 400
    cvs.coords(ball.id,ball.x,ball.y,ball.x+100,ball.y+100)
    root.after(16,main)

root = tkinter.Tk()
root.title('弾む円')
root.geometry('500x500')
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
ball = Circle(200,0)
ball.id = cvs.create_oval(ball.x,ball.y,ball.x+100,ball.y+100,fill='black',width=0)
main()

root.mainloop()