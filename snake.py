import tkinter
import random

key = 'Down'
def key_down(e):
    global key
    key = e.keysym

w,h = 20,20
snake = []
head=(int(w/2),int(h/2))
snake.append(head)
over=False
foods = []
def init_foods():
    for i in range(10):
        while True:
            pos = (random.randint(0,19),random.randint(0,19))
            if not pos in foods and pos != head:
                foods.append(pos)
                break

def draw():
    cvs.delete('snake')
    for body in snake:
        cvs.create_rectangle(body[0]*30,body[1]*30,body[0]*30+30,body[1]*30+30,fill='white',tags='snake')
    for food in foods:
        cvs.create_oval(food[0]*30,food[1]*30,food[0]*30+30,food[1]*30+30,fill='red',width=0,tags=f'{food[0]},{food[1]}')

def move():
    for food in foods:
        if head == food:
            cvs.delete(f'{food[0]},{food[1]}')
            foods.remove(food)
    if len(foods) == 0:
        init_foods()

def main():
    global head,over
    if over:
        fnt=('Times New Roman',30,'bold')
        cvs.create_text(300,300,text='GAME OVER',fill='white',font=fnt)
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
    if head in foods:
        move()
    else:
        snake.pop()
    draw()

    root.after(300, main)

root = tkinter.Tk()
root.title('スネーク')
root.geometry('600x600')
root.bind('<KeyPress>', key_down)
cvs = tkinter.Canvas(root, width=600, height=600, bg='black')
cvs.pack()
init_foods()
main()
root.mainloop()