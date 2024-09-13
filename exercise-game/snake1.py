import tkinter

w,h = 20,20
snake = []
head=(int(w/2),int(h/2))
snake.append(head)
over=False

key = 'Down'
def key_down(e):
    global key
    key = e.keysym

def init_snake():
    for i in range(5):
        snake.insert(0,head)

def draw():
    cvs.delete('snake')
    for body in snake:
        cvs.create_rectangle(body[0]*30,
                             body[1]*30,
                             body[0]*30+30,
                             body[1]*30+30,
                             fill='white',
                             tags='snake')

def main():
    global head,over
    if over:
        fnt=('Times New Roman',30,'bold')
        cvs.create_text(300,300,text='GAME OVER',
                        fill='orange',font=fnt)
        return
    if key == 'Up':
        head = (snake[0][0], snake[0][1]-1)
    if key == 'Down':
        head = (snake[0][0], snake[0][1]+1)
    if key == 'Left':
        head = (snake[0][0]-1, snake[0][1])
    if key == 'Right':
        head = (snake[0][0]+1, snake[0][1])

    if head in snake or head[0]<0 or head[0]>19 or head[1]<0 or head[1]>19:
        over = True

    snake.insert(0,head)
    snake.pop()
    draw()

    root.after(300, main)

root = tkinter.Tk()
root.title('スネーク')
root.geometry('600x600')
root.bind('<KeyPress>', key_down)
cvs = tkinter.Canvas(root, width=600, height=600, bg='black')
cvs.pack()
init_snake()
main()
root.mainloop()