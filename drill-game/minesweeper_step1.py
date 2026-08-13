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

# テスト
for cell in cells:
    if cell.mine:
        cvs.itemconfig(cell.id,fill='#ff0000')

root.mainloop()
