import tkinter
import random

root = tkinter.Tk()
root.title('マインスイーパー')
WIDTH = 500
HEIGHT = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
win_x = (screen_width//2) - (WIDTH//2)
win_y = (screen_height//2) - (HEIGHT//2)
root.geometry(f'{WIDTH}x{HEIGHT}+{win_x}+{win_y}')
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT, bg='gray')
cvs.pack()

class Cell:
    pass

SIZE = 10
MINE_COUNT = 15
cells = []
gameOver = False
openCount = 0

# 盤面を作る
for y in range(SIZE):
    for x in range(SIZE):
        cell = Cell()
        cell.x = x
        cell.y = y
        cell.mine = False
        cell.open = False
        cell.flag = False
        cell.count = 0
        cell.id = cvs.create_rectangle(x*50,y*50,
                            x*50+50,
                            y*50+50,
                            fill='gray',
                            outline='#2f4f4f',
                            width=1)
        cells.append(cell)

# 爆弾を配置(重複しない)
mineCount = 0
while mineCount < MINE_COUNT:
    index = random.randint(0,len(cells)-1)
    cell = cells[index]
    # すでに爆弾があればやり直す
    if cell.mine:
        continue
    cell.mine = True
    mineCount += 1

# 周囲の爆弾数を調べる(隣接する爆弾数を数える)
for cell in cells:
    if cell.mine:
        continue
    count = 0
    for dy in range(-1,2):
        for dx in range(-1,2):
            # 自分自身は除外
            if dx == 0 and dy == 0:
                continue
            x = cell.x + dx
            y = cell.y + dy
            # 盤面の外
            if x < 0 or x >= SIZE or \
                y < 0 or y >= SIZE:
                continue
            neighbor = cells[y*SIZE+x]
            if neighbor.mine:
                count += 1
    cell.count = count

def openCell(event):
    global gameOver,openCount
    if isinstance(event, tkinter.Event):
        for cell in cells:
            if cell.x*50 <= event.x <= cell.x*50+50 and \
            cell.y*50 <= event.y <= cell.y*50+50:
                break
        else:
            return
    else:
        cell = event
    if gameOver: # ゲーム終了後は操作できない
        return
    if cell.open: # すでに開いている
        return
    cell.open = True
    openCount += 1
    # 爆弾だった
    if cell.mine:
        cvs.itemconfig(cell.id,fill='#800000')
        cvs.create_text(cell.x*50+25,
                        cell.y*50+25,
                        text='💣',
                        font=('sans-self',30))
        gameOver = True
        showAllMines()
        cvs.create_text(WIDTH//2,
                        HEIGHT//2,
                        text='ゲームオーバー',
                        fill='#ff0000',
                        font=('sans-self',50))
        return
    # 隣接する爆弾数を表示
    if cell.count > 0:
        cvs.itemconfig(cell.id,fill='#000000')
        cvs.create_text(cell.x*50+25,
                        cell.y*50+25,
                        text=str(cell.count),
                        fill='white',
                        font=('sans-self',30))
    else: # 隣接する爆弾がなければ自動的に開く
        cvs.itemconfig(cell.id,fill='#000000')
        openNeighbors(cell)
    checkClear()

# 隣接しているマスを開く
def openNeighbors(cell):
    for dy in range(-1,2):
        for dx in range(-1,2):
            if dx == 0 and dy == 0:
                continue
            # 自分自身は除外
            if dx == 0 and dy == 0:
                continue
            x = cell.x + dx
            y = cell.y + dy
            # 盤面の外
            if x < 0 or x >= SIZE or \
                y < 0 or y >= SIZE:
                continue
            neighbor = cells[y*SIZE+x]
            if not neighbor.mine and \
            not neighbor.open and \
            not neighbor.flag:
                openCell(neighbor)

# 爆弾をすべて表示
def showAllMines():
    for cell in cells:
        if cell.mine:
            cvs.itemconfig(cell.id,fill='#800000')
            cvs.create_text(cell.x*50+25,
                            cell.y*50+25,
                            text='💣',
                            font=('sans-self',30))

# クリア判定
def checkClear():
    safeCellCount = SIZE*SIZE-MINE_COUNT
    if openCount == safeCellCount:
        cvs.create_text(WIDTH//2,
                        HEIGHT//2,
                        text='🎉クリア！',
                        fill='#ff0000',
                        font=('sans-self',50))

root.bind('<Button-1>', openCell)
root.mainloop()
