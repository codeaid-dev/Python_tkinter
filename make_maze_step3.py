import tkinter
import random, time

mazew,mazeh = 17,17
maze = [[0 for x in range(mazew)] for y in range(mazeh)]
def make_maze():
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for y in range(mazeh):
        for x in range(mazew):
            maze[y][x] = 0
    #周りの壁を作る
    for x in range(17):
        maze[0][x] = 1
        maze[mazeh-1][x] = 1
    for y in range(1,mazeh-1):
        maze[y][0] = 1
        maze[y][mazew-1] = 1
    #柱を建てて壁を作る
    for y in range(2,mazeh-2,2):
        for x in range(2,mazew-2,2):
            maze[y][x] = 1
            d = random.randint(0,2)
            if y == 2:
                d = random.randint(0,3)
            maze[y+dy[d]][x+dx[d]] = 1

def show_maze():
    cvs.delete('all')
    for y in range(mazeh):
        for x in range(mazew):
            if maze[y][x] == 1:
                cvs.create_rectangle(x*50,y*50, x*50+50, y*50+50, fill='gray', width=0)

goal_x,goal_y = 1,1
def set_goal():
    global goal_x,goal_y
    while True:
        goal_x = random.randint(1,mazew-2)
        goal_y = random.randint(1,mazeh-2)
        if maze[goal_y][goal_x] == 0:
            break

def main():
    global goal,start
    make_maze()
    show_maze()
    player.x = 1
    player.y = 1
    player.id = cvs.create_oval(player.x*50,player.y*50,player.x*50+50,player.y*50+50,fill='blue',width=0)
    goal = False
    set_goal()
    start = time.time()

class Circle():
    pass

goal = False
def key_down(e):
    global goal
    if goal:
        return
    x, y = player.x, player.y
    key = e.keysym
    if key == 'Up' and maze[y-1][x] == 0:
        player.y -= 1
    if key == 'Down' and maze[y+1][x] == 0:
        player.y += 1
    if key == 'Left' and maze[y][x-1] == 0:
        player.x -= 1
    if key == 'Right' and maze[y][x+1] == 0:
        player.x += 1
    cvs.coords(player.id,player.x*50,player.y*50,player.x*50+50,player.y*50+50)
    if player.y==goal_y and player.x==goal_x:
        cvs.itemconfig(player.id,fill='yellow')
        end = int(time.time()-start)
        cvs.create_text(425,400,text='GOAL',fill='red',font=('Helvetica',50))
        cvs.create_text(425,450,text=f'time: {end}sec',fill='red',font=('Helvetica',50))
        goal = True

root = tkinter.Tk()
root.title('自動迷路生成')
root.bind('<KeyPress>', key_down)
cvs = tkinter.Canvas(width=850, height=850, bg='white')
cvs.pack()
menu = tkinter.Menu(root)
menu_comm = tkinter.Menu(menu,tearoff=0)
menu_comm.add_command(label='Restart',command=main)
menu.add_cascade(label='Main',menu=menu_comm)
root.config(menu=menu)
player = Circle()
main()

root.mainloop()