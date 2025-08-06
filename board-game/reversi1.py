import tkinter

GRID_SIZE = 8
CELL_SIZE = 100
EMPTY = 0
BLACK = 1
WHITE = 2
board = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
board[3][3] = WHITE
board[4][4] = WHITE
board[3][4] = BLACK
board[4][3] = BLACK
WIDTH,HEIGHT = 800,800
root = tkinter.Tk()
root.title("リバーシ(オセロ)")
cvs = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg='#008000')
cvs.pack()

def draw_board():
    for i in range(GRID_SIZE+1):
        cvs.create_line(i*CELL_SIZE,0,
                        i*CELL_SIZE,HEIGHT,
                        fill='black',width=2)
        cvs.create_line(0,i*CELL_SIZE,
                        WIDTH,i*CELL_SIZE,
                        fill='black',width=2)

def draw_pieces():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == BLACK:
                cvs.create_oval(i*CELL_SIZE+3,
                                j*CELL_SIZE+3,
                                i*CELL_SIZE+CELL_SIZE-3,
                                j*CELL_SIZE+CELL_SIZE-3,
                                fill='black',
                                width=0,tags='pieces')
            elif board[i][j] == WHITE:
                cvs.create_oval(i*CELL_SIZE+3,
                                j*CELL_SIZE+3,
                                i*CELL_SIZE+CELL_SIZE-3,
                                j*CELL_SIZE+CELL_SIZE-3,
                                fill='white',
                                width=0,tags='pieces')

draw_board()
draw_pieces()
root.mainloop()
