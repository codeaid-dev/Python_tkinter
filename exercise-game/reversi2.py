import tkinter

GRID_SIZE = 8
CELL_SIZE = 100
EMPTY = 0
BLACK = 1
WHITE = 2
board = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = BLACK
DIR8 = [(-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)]
WIDTH,HEIGHT = 800,800

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

def flip_pieces(x, y, dx, dy, player):
    nx,ny = x+dx,y+dy
    pieces_to_flip = []
    
    while on_board(nx, ny) and \
            board[nx][ny] == (WHITE if player==BLACK else BLACK):
        pieces_to_flip.append((nx, ny))
        nx+=dx
        ny+=dy
    
    if on_board(nx, ny) and board[nx][ny] == player:
        for fx, fy in pieces_to_flip:
            board[fx][fy] = player

def on_board(x, y):
    return 0<=x<GRID_SIZE and 0<=y<GRID_SIZE

def make_move(x, y, player):
    board[x][y] = player
    for dx, dy in DIR8:
        flip_pieces(x, y, dx, dy, player)

def valid_move(x, y, player):
    if board[x][y] != EMPTY:
        return False

    for dx,dy in DIR8:
        nx,ny = x+dx,y+dy
        if on_board(nx, ny) and \
            board[nx][ny] == (WHITE if player==BLACK else BLACK):
            while on_board(nx, ny) and board[nx][ny] != EMPTY:
                if board[nx][ny] == player:
                    return True
                nx+=dx
                ny+=dy
    return False

def reset():
    global current_player
    current_player = BLACK
    cvs.delete('pieces')
    for i in range(GRID_SIZE*GRID_SIZE):
        x,y = i%8,i//8
        board[x][y] = 0
    board[3][3] = WHITE
    board[4][4] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK

def pressed(event):
    global current_player
    x = event.x//CELL_SIZE
    y = event.y//CELL_SIZE
    if valid_move(x, y, current_player):
        make_move(x, y, current_player)
        current_player = \
        WHITE if current_player==BLACK else BLACK
    draw_pieces()

def key(event):
    if event.keysym.upper() == 'R':
        reset()
        draw_pieces()

root = tkinter.Tk()
root.title("リバーシ(オセロ)")
root.bind('<Button>',pressed)
root.bind('<Key>', key)
cvs = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg='#008000')
cvs.pack()
reset()
draw_board()
draw_pieces()
root.mainloop()
