import pygame

import time

import sys

board = [['  ' for i in range(23)] for i in range(16)]

## Creates a chess piece class that shows what team a piece is on, what type of piece it is and whether or not it can be killed by another selected piece.
class Piece:
    def __init__(self, team, type, image,dynamite, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image
        self.dynamite = dynamite



## Creates instances of chess pieces, so far we got: pawn, king, rook and bishop
## The first parameter defines what team its on and the second, what type of piece it is
bp = Piece('b', 'p', 'images/b_pawn.png',False)
wp = Piece('w', 'p', 'images/w_pawn.png',False)
wpB = Piece('w','p','images/w_pawnDynamite.png',False)
bpB = Piece('b','p','images/b_pawnDynamite.png',False)
bk = Piece('b', 'k', 'images/b_king.png',False)
wk = Piece('w', 'k', 'images/w_king.png',False)
br = Piece('b', 'r', 'images/b_rook.png',False)
wr = Piece('w', 'r', 'images/w_rook.png',False)
bb = Piece('b', 'b', 'images/b_bishop.png',False)
wb = Piece('w', 'b', 'images/w_bishop.png',False)
bq = Piece('b', 'q', 'images/b_queen.png',False)
wq = Piece('w', 'q', 'images/w_queen.png',False)
bkn = Piece('b', 'kn', 'images/b_knight.png',False)
wkn = Piece('w', 'kn', 'images/w_knight.png',False)
rp = Piece('r', 'p', 'images/r_pawn.png',False)
rpB = Piece('r', 'p', 'images/r_pawnDynamite.png',False)
rk = Piece('r', 'k', 'images/r_king.png',False)
rr = Piece('r', 'r', 'images/r_rook.png',False)
rb = Piece('r', 'b', 'images/r_bishop.png',False)
rq = Piece('r', 'q', 'images/r_queen.png',False)
rkn = Piece('r', 'kn', 'images/r_knight.png',False)

up = Piece('u', 'p', 'images/u_pawn.png',False)
upB = Piece('u', 'p', 'images/u_pawnDynamite.png',False )
uk = Piece('u', 'kn', 'images/u_king.png',False)
ur = Piece('u', 'r', 'images/u_rook.png',False)
ub = Piece('u', 'b', 'images/u_bishop.png',False)
uq = Piece('u', 'q', 'images/u_queen.png',False)
ukn = Piece('u', 'kn', 'images/u_knight.png',False)

yp = Piece('y', 'p', 'images/y_pawn.png',False)
ypB = Piece('y', 'p', 'images/y_pawnDynamite.png',False)
yk = Piece('y', 'kn', 'images/y_king.png',False)
yr = Piece('y', 'r', 'images/y_rook.png',False)
yb = Piece('y', 'b', 'images/y_bishop.png',False)
yq = Piece('y', 'q', 'images/y_queen.png',False)
ykn = Piece('y', 'kn', 'images/y_knight.png',False)

gp = Piece('g', 'p', 'images/g_pawn.png',False)
gk = Piece('g', 'kn', 'images/g_king.png',False)
gr = Piece('g', 'r', 'images/g_rook.png',False)
gb = Piece('g', 'b', 'images/g_bishop.png',False)
gq = Piece('g', 'q', 'images/g_queen.png',False)
gkn = Piece('g', 'kn', 'images/g_knight.png',False)
gpB = Piece('g', 'p', 'images/g_pawnDynamite.png',False)

starting_order = {(0,0):None,(0,1): None,(0,2):None,(0,3): None,(0,4): None,(0,5):None,(0,6): None,(0,7): None,(0,8): None,(0,9): None,(0,10): None,(0,11): None,(0,12): None,(0,13): None,(0,14): None,(0,15): None,(1,0): None,(1,1): None,(1,2): None,(1,3): None,(1,4): None,(1,5): None,(1,6): None,(1,7): None,(1,8): None,(1,9): None,(1,10): None,(1,11): None,(1,12): None,(1,13): None,(1,14): None,(1,15): None,(2,0): None,(2,1): None,(2,2): None,(2,3): None,(2,4): None,(2,5): None,(2,6): None,(2,7): None,(2,8): None,(2,9): None,(2,10): None,(2,11): None,(2,12): None,(2,13): None,(2,14): None,(2,15): None,(3,0): None,(3,1): None,(3,2): None,(3,3): None,(3,4): None,(3,5): None,(3,6): None,(3,7): None,(3,8): None,(3,9): None,(3,10): None,(3,11): None,(3,12): None,(3,13): None,(3,14):None,(3,15): None,(4,0): None,(4,1): None,(4,2): None,(4,3): None,(4,4): None,(4,5): None,(4,6): None,(4,7): None,(4,8): None,(4,9): None,(4,10): None,(4,11): None,(4,12): None,(4,13): None,(4,14):None,(4,15): None,(5,0): None,(5,1): None,(5,2): None,(5,3): None,(5,4): None,(5,5): None,(5,6): None,(5,7): None,(5,8): None,(5,9): None,(5,10): None,(5,11): None,(5,12): None,(5,13): None,(5,14):None,(5,15): None,(6,0): None,(6,1): None,(6,2): None,(6,3): None,(6,4): None,(6,5): None,(6,6): None,(6,7): None,(6,8): None,(6,9): None,(6,10): None,(6,11): None,(6,12): None,(6,13): None,(6,14): None,(6,15): None,(7,0): None,(7,1): None,(7,2): None,(7,3): None,(7,4): None,(7,5): None,(7,6): None,(7,7): None,(7,8): None,(7,9): None,(7,10): None,(7,11): None,(7,12):None,(7,13): None,(7,14): None,(7,15): None,(8,0): None,(8,1): None,(8,2): None,(8,3): None,(8,4): None,(8,5): None,(8,6): None,(8,7): None,(8,8): None,(8,9): None,(8,10): None,(8,11): None,(8,12): None,(8,13): None,(8,14):  None,(8,15): None,(9,0): None,(9,1):None,(9,2): None,(9,3): None,(9,4): None,(9,5): None,(9,6): None,(9,7): None,(9,8): None,(9,9): None,(9,10): None,(9,11): None,(9,12): None,(9,13): None,(9,14): None,(9,15):None,(10,0): None,(10,1): None,(10,2): None,(10,3): None,(10,4): None,(10,5): None,(10,6): None,(10,7): None,(10,8): None,(10,9): None,(10,10): None,(10,11): None,(10,12): None,(10,13): None,(10,14): None,(10,15): None,(11,0): None,(11,1): None,(11,2): None,(11,3): None,(11,4): None,(11,5): None,(11,6): None,(11,7): None,(11,8): None,(11,9): None,(11,10): None,(11,11): None,(11,12): None,(11,13): None,(11,14):  None,(11,15): None,(12,0): None,(12,1): None,(12,2):None,(12,3):None,(12,4): None,(12,5): None,(12,6): None,(12,7): None,(12,8): None,(12,9): None,(12,10): None,(12,11): None,(12,12): None,(12,13): None,(12,14):  None,(12,15): None,(13,0): None,(13,1): None,(13,2): None,(13,3): None,(13,4): None,(13,5): None,(13,6): None,(13,7): None,(13,8): None,(13,9): None,(13,10): None,(13,11): None,(13,12): None,(13,13): None,(13,14):None,(13,15): None,(14,0): None,(14,1): None,(14,2): None,(14,3): None,(14,4): None,(14,5): None,(14,6): None,(14,7): None,(14,8): None,(14,9): None,(14,10): None,(14,11): None,(14,12): None,(14,13): None,(14,14): None,(14,15): None,(15,0): None,(15,1): None,(15,2): None,(15,3): None,(15,4): None,(15,5): None,(15,6):None,(15,7): None,(15,8): None,(15,9): None,(15,10): None,(15,11): None,(15,12): None,(15,13):None,(15,14): None,(15,15): None,(16,0): None,(16,1): None,(16,2): None,(16,3): None,(16,4): None,(16,5): None,(16,6): None,(16,7): None,(16,8): None,(16,9): None,(16,10): None,(16,11): None,(16,12): None,(16,13):None,(16,14): None,(16,15): None,(17,0): None,(17,1): None,(17,2): None,(17,3): None,(17,4): None,(17,5): None,(17,6): None,(17,7): None,(17,8): None,(17,9): None,(17,10): None,(17,11): None,(17,12): None,(17,13):None,(17,14):None,(17,15): None,(18,0): None,(18,1): None,(18,2): None,(18,3): None,(18,4): None,(18,5): None,(18,6): None,(18,7): None,(18,8): None,(18,9): None,(18,10): None,(18,11): None,(18,12): None,(18,13): None,(18,14): None,(18,15): None,(19,0): None,(19,1): None,(19,2): None,(19,3): None,(19,4): None,(19,5): None,(19,6):None,(19,7): None,(19,8): None,(19,9): None,(19,10): None,(19,11): None,(19,12): None,(19,13): None,(19,14):  None,(19,15):  None,(20,0): None,(20,1): None,(20,2): None,(20,3): None,(20,4): None,(20,5): None,(20,6): None,(20,7): None,(20,8): None,(20,9): None,(20,10): None,(20,11): None,(20,12): None,(20,13): None,(20,14): None,(20,15):  None,(21,0):  None,(21,1): None,(21,2):None,(21,3): None,(21,4):None,(21,5): None,(21,6): None,(21,7): None,(21,8): None,(21,9): None,(21,10): None,(21,11): None,(21,12): None,(21,13):  None,(21,14):  None,(21,15): None,(22,0):  None,(22,1): None,(22,2): None,(22,3):  None,(22,4): None,(22,5): None,(22,6): None,(22,7):None,(22,8): None,(22,9): None,(22,10): None,(22,11): None,(22,12): None,(22,13):  None,(22,14): None,(22,15): None}


## returns the input if the input is within the boundaries of the board
def on_board(position):
    if position[0] > -1 and position[1] > -1 and position[0] < 16 and position[1] < 23:
        return True


walls = []
def check_wall(position):

    if [position[0],position[1]] not in walls:
        return True

## returns a string that places the rows and columns of the board in a readable manner
def convert_to_readable(board):
    output = ''

    for i in board:
        for j in i:
            try:
                output += j.team + j.type + ', '
            except:
                output += j + ', '
        output += '\n'
    return output


## resets "x's" and killable pieces
def deselect():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'x ':
                board[row][column] = '  '
            else:
                try:
                    board[row][column].killable = False
                except:
                    pass
    return convert_to_readable(board)


## Takes in board as argument then returns 2d array containing positions of valid moves
def highlight(board):
    highlighted = []
    for i in range(len(board) ):
        for j in range(len(board[0])):
            if board[i][j] == 'x ':
                highlighted.append((i, j))
            else:
                try:
                    if board[i][j].killable:
                        highlighted.append((i, j))
                except:
                    pass
    return highlighted
def check_team(moves, index):
    row, col = index

    if moves%6 == 0:
        if board[row][col].team == 'w':
                return True
    elif moves%6 == 1:
        if board[row][col].team == 'b':
            return True
    elif moves%6 == 2:
        if board[row][col].team == 'y':
            return True
    elif moves%6 == 3:
        if board[row][col].team == 'r':
                 return True
    elif moves%6 == 4:
        if board[row][col].team == 'u':
            return True
    elif moves%6 == 5:
        if board[row][col].team == 'g':
            return True

## This takes in a piece object and its index then runs then checks where that piece can move using separately defined functions for each type of piece.
def select_moves(piece, index, moves):
    if check_team(moves, index):

        if piece.type == 'p':
            return highlight(pawn_moves_w(index))
        if piece.type == 'k':
            return highlight(king_moves(index))

        if piece.type == 'r':
            return highlight(rook_moves(index))

        if piece.type == 'b':
            return highlight(bishop_moves(index))

        if piece.type == 'q':
            return highlight(queen_moves(index))

        if piece.type == 'kn':
            return highlight(knight_moves(index))


## Basically, check black and white pawns separately and checks the square above them. If its free that space gets an "x" and if it is occupied by a piece of the opposite team then that piece becomes killable.
def pawn_moves_b(index):


    bottom3 = [[(index[0]+1),(index[1] +1)],[(index[0]+1),(index[1] -1)],[(index[0]-1),(index[1] +1)],[(index[0]-1),(index[1] -1)],[(index[0]+1),(index[1])],[(index[0]),(index[1] +1)],[(index[0]-1),index[1]],[index[0],index[1]-1]]

    for positions in bottom3:
        if on_board(positions) and check_wall(positions):
            if board[positions[0]][positions[1]] == '  ':
                board[positions[0]][positions[1]] = 'x '
            elif (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                board[positions[0]][positions[1]].killable = True
    return board

def pawn_moves_w(index):

    top3 = [[(index[0]+1),(index[1] +1)],[(index[0]+1),(index[1] -1)],[(index[0]-1),(index[1] +1)],[(index[0]-1),(index[1] -1)],[(index[0]+1),(index[1])],[(index[0]),(index[1] +1)],[(index[0]-1),index[1]],[index[0],index[1]-1]]

    for positions in top3:
        if on_board(positions):
            if board[index[0]][index[1]].dynamite:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                elif (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                    board[positions[0]][positions[1]].killable = True
            elif(check_wall(positions)):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                elif (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                    board[positions[0]][positions[1]].killable = True


    return board



## This just checks a 3x3 tile surrounding the king. Empty spots get an "x" and pieces of the opposite team become killable.
def king_moves(index):
    for y in range(3):
        for x in range(3):
            if on_board((index[0] - 1 + y, index[1] - 1 + x)) and check_wall((index[0] - 1 + y, index[1] - 1 + x)):
                if board[index[0] - 1 + y][index[1] - 1 + x] == '  ':
                    board[index[0] - 1 + y][index[1] - 1 + x] = 'x '
                else:
                    if board[index[0] - 1 + y][index[1] - 1 + x].team != board[index[0]][index[1]].team:
                        board[index[0] - 1 + y][index[1] - 1 + x].killable = True
    return board


## This creates 4 lists for up, down, left and right and checks all those spaces for pieces of the opposite team. The list comprehension is pretty long so if you don't get it just msg me.
def rook_moves(index):
    cross = [[[index[0] + i, index[1]] for i in range(1, 17)],
             [[index[0] - i, index[1]] for i in range(1,17)],
             [[index[0], index[1] + i] for i in range(1, 24)],
             [[index[0], index[1] - i] for i in range(1, 24)]]

    for direction in cross:
        for positions in direction:
            if on_board(positions) and board[index[0]][index[1]].dynamite:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].killable = True
                    break
            elif(check_wall(positions) and on_board(positions)):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                        board[positions[0]][positions[1]].killable = True
                    break
            else:
                break
    return board


## Same as the rook but this time it creates 4 lists for the diagonal directions and so the list comprehension is a little bit trickier.
def bishop_moves(index):
    diagonals = [[[index[0] - i,index[1] + i] for i in range(1,23)],
                [[index[0] - i,index[1] - i] for i in range(1,23)],
                [[index[0] + i,index[1] + i] for i in range(1,23)],
                [[index[0] + i,index[1] - i] for i in range(1,23)]]

    for dia in diagonals:
        for positions in dia:

            if on_board(positions) and board[index[0]][index[1]].dynamite:

                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '

                else:
                    if (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                        board[positions[0]][positions[1]].killable = True
                    break
            elif (on_board(positions) and check_wall(positions)):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '

                else:
                    if (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                        board[positions[0]][positions[1]].killable = True
                    break
            else:
                break

    return board


## applies the rook moves to the board then the bishop moves because a queen is basically a rook and bishop in the same position.
def queen_moves(index):
    board = rook_moves(index)
    board = bishop_moves(index)
    return board



## Checks a 5x5 grid around the piece and uses pythagoras to see if if a move is valid. Valid moves will be a distance of sqrt(5) from centre
def knight_moves(index):

    knight_moves = [[(index[0]-2),(index[1] +1)], [(index[0]-2),(index[1]-1)],[(index[0]-1), (index[1] + 2)],[(index[0]-1), (index[1] - 2)],[(index[0] + 1),(index[1] - 2)], [(index[0]+2),(index[1]-1)], [(index[0]+1),(index[1]+2)],[(index[0]+2),(index[1]+1)]]
    for move in knight_moves:
        if on_board(move) and check_wall(move) :

            if board[move[0]][move[1]] == '  ':
                board[move[0]][move[1]] = 'x '

            elif (board[move[0]][move[1]].team != board[index[0]][index[1]].team):
                board[move[0]][move[1]].killable = True


    return board


WIDTH = 826

WIN = pygame.display.set_mode((1000, 560))

""" This is creating the window that we are playing on, it takes a tuple argument which is the dimensions of the window so in this case 800 x 800px
"""

pygame.display.set_caption("Chess")
WHITE = (236, 222, 183)
GREY = (137, 115, 91)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.occupied = None


    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / 23, WIDTH / 23))

    def drawWall(self, WIN):
        pygame.draw.rect(WIN, BLACK, (self.x, self.y, WIDTH / 23, WIDTH / 23))
    def setup(self, WIN):
        if starting_order[(self.row, self.col)]:
            if starting_order[(self.row, self.col)] == None:
                pass
            else:
                WIN.blit(starting_order[(self.row, self.col)], (self.x, self.y))

        """
        For now it is drawing a rectangle but eventually we are going to need it
        to use blit to draw the chess pieces instead
        """


def make_grid(rows, width):
    grid = []
    gap = WIDTH // rows


    for i in range(16):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            if [i,j] not in walls:
                if (i+j)%2 ==1:
                    grid[i][j].colour = GREY
            else:
                grid[i][j].colour = BLACK
    return grid
"""
This is creating the nodes thats are on the board(so the chess tiles)
I've put them into a 2d array which is identical to the dimesions of the chessboard
"""


def draw_grid(win, rows, width):
    gap = width // 23
    for i in range(16):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

    """
    The nodes are all white so this we need to draw the grey lines that separate all the chess tiles
    from each other and that is what this function does"""


def update_display(win, grid, rows, width):

    for row in grid:
        for spot in row:
            if([spot.col, spot.row] not in walls):
                spot.draw(win)
                spot.setup(win)
            else:
                spot.drawWall(win)

                spot.setup(win)
    draw_grid(win, rows, width)


    pygame.display.update()


def Find_Node(pos, WIDTH):
    interval = 826 // 23
    y,x = pos
    rows = x // (560 // 16)
    columns = y // interval

    return  int(columns),int(rows)


def display_potential_moves(positions, grid):
    for i in positions:
        x, y = i
        grid[x][y].colour = BLUE
        """
        Displays all the potential moves
        """


def Do_Move(OriginalPos, FinalPosition, WIN):
    starting_order[FinalPosition] = starting_order[OriginalPos]
    starting_order[OriginalPos] = None


def remove_highlight(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i+j)%2 == 0:
                grid[i][j].colour = WHITE
            else:
                grid[i][j].colour = GREY
    return grid
"""this takes in 2 co-ordinate parameters which you can get as the position of the piece and then the position of the node it is moving to
you can get those co-ordinates using my old function for swap"""



def main(WIN, WIDTH,board):
    moves = 0
    selected = False
    piece_to_move=[]

    grid = make_grid(23, WIDTH)
    placeWalls(WIN,WIDTH)
    placeWhite(WIN,WIDTH,board)
    print(board)
    while True:
        pygame.time.delay(50) ##stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            """This quits the program if the player closes the window"""

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                y,x = Find_Node(pos, WIDTH)

                if selected == False:
                    try:

                        possible = select_moves((board[x][y]), (x,y), moves)

                        for positions in possible:
                            row, col = positions

                            grid[row][col].colour = BLUE
                        piece_to_move = x,y
                        selected = True
                    except:
                        piece_to_move = []
                        print('Can\'t select')
                    #print(piece_to_move)

                else:
                    try:
                        if board[x][y].killable == True:
                            row, col = piece_to_move ## coords of original piece
                            board[x][y] = board[row][col]
                            board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), WIN)

                            moves += 1
                            print(convert_to_readable(board))
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Deselected")
                    except:
                        if board[x][y] == 'x ':
                            row, col = piece_to_move
                            print(row,col)

                            board[x][y] = board[row][col]
                            board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            if not (check_wall([x,y])) and board[x][y].dynamite:
                                walls.remove([x,y])
                                board[x][y].dynamite = False

                            Do_Move((col, row), (y, x), WIN)

                            moves += 1
                            print(convert_to_readable(board))

                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Invalid move")
                    selected = False

            update_display(WIN, grid, 23, WIDTH)

def placeWalls(WIN,WIDTH):
    test = True
    while test == True:
        grid = make_grid(23, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                y, x = Find_Node(pos, WIDTH)
                if [x,y] in walls:
                    walls.remove([x,y])
                else:
                    walls.append([x,y])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    test = False


        update_display(WIN, grid, 23, WIDTH)

def placeWhite(WIN,WIDTH,board):

    pygame.display.update()
    pieces = [wp.image,wp.image,wp.image,wp.image,wkn.image,wkn.image, wq.image, wk.image, wr.image, wr.image,wb.image,wb.image, bp.image,bp.image,bp.image,bp.image,bkn.image,bkn.image, bq.image, bk.image, br.image, br.image,bb.image,bb.image, yp.image,yp.image,yp.image,yp.image,ykn.image,ykn.image, yq.image, yk.image, yr.image, yr.image,yb.image,yb.image, rp.image,rp.image,rp.image,rp.image,rkn.image,rkn.image, rq.image, rk.image, rr.image, rr.image,rb.image,rb.image, up.image,up.image,up.image,up.image,ukn.image,ukn.image, uq.image, uk.image, ur.image, ur.image,ub.image,ub.image, gp.image,gp.image,gp.image,gp.image,gkn.image,gkn.image, gq.image, gk.image, gr.image, gr.image,gb.image,gb.image,]
    piecesDetails = [Piece('w', 'p', 'images/w_pawn.png',False),Piece('w', 'p', 'images/w_pawn.png',False),Piece('w', 'p', 'images/w_pawn.png',False),Piece('w', 'p', 'images/w_pawn.png',False), Piece('w', 'kn', 'images/w_knight.png',False),Piece('w', 'kn', 'images/w_knight.png',False),Piece('w', 'q', 'images/w_queen.png',False), Piece('w', 'k', 'images/w_king.png',False), Piece('w', 'r', 'images/w_rook.png',False), Piece('w', 'r', 'images/w_rook.png',False), Piece('w', 'b', 'images/w_bishop.png',False),Piece('w', 'b', 'images/w_bishop.png',False),    Piece('b', 'p', 'images/b_pawn.png',False),Piece('b', 'p', 'images/b_pawn.png',False),Piece('b', 'p', 'images/b_pawn.png',False),Piece('b', 'p', 'images/b_pawn.png',False), Piece('b', 'kn', 'images/b_knight.png',False),Piece('b', 'kn', 'images/b_knight.png',False),Piece('b', 'q', 'images/b_queen.png',False), Piece('b', 'k', 'images/b_king.png',False), Piece('b', 'r', 'images/b_rook.png',False), Piece('b', 'r', 'images/b_rook.png',False), Piece('b', 'b', 'images/b_bishop.png',False),Piece('b', 'b', 'images/b_bishop.png',False), Piece('y', 'p', 'images/y_pawn.png',False), Piece('y', 'p', 'images/y_pawn.png',False), Piece('y', 'p', 'images/y_pawn.png',False), Piece('y', 'p', 'images/y_pawn.png',False), Piece('y', 'kn', 'images/y_knight.png',False),  Piece('y', 'kn', 'images/y_knight.png',False), Piece('y', 'q', 'images/y_queen.png',False), Piece('y', 'k', 'images/y_king.png',False), Piece('y', 'r', 'images/y_rook.png',False), Piece('y', 'r', 'images/y_rook.png',False), Piece('y', 'b', 'images/y_bishop.png',False), Piece('y', 'b', 'images/y_bishop.png',False), Piece('r', 'p', 'images/r_pawn.png',False), Piece('r', 'p', 'images/r_pawn.png',False),Piece('r', 'p', 'images/r_pawn.png',False),Piece('r', 'p', 'images/r_pawn.png',False), Piece('r', 'kn', 'images/r_knight.png',False), Piece('r', 'kn', 'images/r_knight.png',False), Piece('r', 'q', 'images/r_queen.png',False), Piece('r', 'k', 'images/r_king.png',False), Piece('r', 'r', 'images/r_rook.png',False), Piece('r', 'r', 'images/r_rook.png',False), Piece('r', 'b', 'images/r_bishop.png',False), Piece('r', 'b', 'images/r_bishop.png',False), Piece('u', 'p', 'images/u_pawn.png',False), Piece('u', 'p', 'images/u_pawn.png',False), Piece('u', 'p', 'images/u_pawn.png',False), Piece('u', 'p', 'images/u_pawn.png',False), Piece('u', 'kn', 'images/u_knight.png',False), Piece('u', 'kn', 'images/u_knight.png',False), Piece('u', 'q', 'images/u_queen.png',False), Piece('u', 'k', 'images/u_king.png',False), Piece('u', 'r', 'images/u_rook.png',False), Piece('u', 'r', 'images/u_rook.png',False), Piece('u', 'b', 'images/u_bishop.png',False),  Piece('u', 'b', 'images/u_bishop.png',False), Piece('g', 'p', 'images/g_pawn.png',False), Piece('g', 'p', 'images/g_pawn.png',False), Piece('g', 'p', 'images/g_pawn.png',False), Piece('g', 'p', 'images/g_pawn.png',False), Piece('g', 'kn', 'images/g_knight.png',False), Piece('g', 'kn', 'images/g_knight.png',False), Piece('g', 'q', 'images/g_queen.png',False), Piece('g', 'k', 'images/g_king.png',False), Piece('g', 'r', 'images/g_rook.png',False), Piece('g', 'r', 'images/g_rook.png',False), Piece('g', 'b', 'images/g_bishop.png',False),  Piece('g', 'b', 'images/g_bishop.png',False)]

    counter = 0
    WIN.blit(pygame.image.load(pieces[counter]), (900,100))
    while True:
        grid = make_grid(23, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                y, x = Find_Node(pos, WIDTH)
                starting_order.update({(y,x): pygame.transform.scale(pygame.image.load(pieces[counter]),(30,30))})
                board[x][y] = piecesDetails[counter]
                #starting_order.update({(0,0):pygame.transform.scale(pygame.image.load(wp.image),(30,30))})
                counter += 1

                if (counter==72):
                    update_display(WIN, grid, 23, WIDTH)

                    return board
                else:
                    WIN.fill(BLACK)
                    WIN.blit(pygame.image.load(pieces[counter]), (900,100))

        update_display(WIN, grid, 23, WIDTH)


main(WIN,WIDTH,board)
