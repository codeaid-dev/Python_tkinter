import tkinter, random

class Circle:
    def __init__(self):
        self.x = random.randint(0,450)
        self.y = 0
        self.speed = random.randint(0,5)
        self.gravity = 0.05

def main():
    for ball in balls:
        ball.y += ball.speed
        ball.speed += ball.gravity
        if ball.y+50>500:
            ball.speed *= -0.85
            # ball.speed *= -0.98
            ball.y = 450
        cvs.coords(ball.id,ball.x,ball.y,ball.x+50,ball.y+50)
    root.after(16,main)

root = tkinter.Tk()
root.title('弾む円')
root.geometry('500x500')
cvs = tkinter.Canvas(root,width=500,height=500,bg='white')
cvs.pack()
balls = []
for i in range(6):
    ball = Circle()
    color = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
    ball.id = cvs.create_oval(ball.x,ball.y,ball.x+50,ball.y+50,fill=color,width=0)
    balls.append(ball)
main()

root.mainloop()