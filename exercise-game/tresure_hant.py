import tkinter
import tkinter.messagebox
import random

mazew,mazeh = 17,17
maze = [[0 for x in range(mazew)] for y in range(mazeh)]
def make_maze():
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    #周りの壁を作る
    for x in range(17):
        maze[0][x] = 1
        maze[mazeh-1][x] = 1
    for y in range(1,mazeh-1):
        maze[y][0] = 1
        maze[y][mazew-1] = 1
    #内側をクリアする
    for y in range(1,mazeh-1):
        for x in range(1,mazew-1):
            maze[y][x] = 0
    #柱を建てて壁を作る
    for y in range(2,mazeh-2,2):
        for x in range(2,mazew-2,2):
            maze[y][x] = 1
            d = random.randint(0,2)
            if y == 2:
                d = random.randint(0,3)
            maze[y+dy[d]][x+dx[d]] = 1

#宝をセットする
tresurex,tresurey = 1,1
def set_tresure():
    global tresurex,tresurey
    while True:
        tresurex = random.randint(1,mazew-2)
        tresurey = random.randint(1,mazeh-2)
        if maze[tresurey][tresurex] == 0:
            break

#キーイベント取得(押されたキーを判定しキャラクターを動かす)
posx,posy = 1,1
def key_down(e):
    global posx,posy
    key = e.keysym
    if key == 'Up' and maze[posy-1][posx] == 0:
        posy = posy - 1
    if key == 'Down' and maze[posy+1][posx] == 0:
        posy = posy + 1
    if key == 'Left' and maze[posy][posx-1] == 0:
        posx = posx - 1
    if key == 'Right' and maze[posy][posx+1] == 0:
        posx = posx + 1
    canvas.delete('PLAYER')
    canvas.create_image(posx*50+25, posy*50+25, image=img, tag='PLAYER')
    if posy == tresurey and posx == tresurex:
        canvas.create_image(posx*50+25, posy*50+25, image=tresure_img, tag='TAKARA')
        canvas.update()
        tkinter.messagebox.showinfo('おめでとう','宝を見つけた！')

#2000ms(2秒)ごとに関数を実行(宝を見つけたときと、時間切れをチェックする)
blockx = 0
def timer():
    global blockx
    if maze[0][blockx] == 1:
        maze[0][blockx] = 2
        canvas.create_rectangle(blockx*50,0, blockx*50+50, 50, fill='red', width=0)
        if blockx < mazew-1:
            blockx += 1
    if maze[0][mazew-1] == 2:
        canvas.update()
        tkinter.messagebox.showinfo('タイマー','時間切れ！')
    else:
        root.after(2000, timer)

root = tkinter.Tk()
root.title('宝探し')
root.bind('<KeyPress>', key_down)
canvas = tkinter.Canvas(width=850, height=850, bg='white')
canvas.pack()

make_maze()
for y in range(mazeh):
    for x in range(mazew):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*50,y*50, x*50+50, y*50+50, fill='gray', width=0)
set_tresure()
tresure_img = tkinter.PhotoImage(file='images/tresure_50x50.png')
img = tkinter.PhotoImage(file='images/inu_50x50.png')
canvas.create_image(posx*50+25, posy*50+25, image=img, tag='PLAYER')
timer()
root.mainloop()
