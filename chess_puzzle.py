from copy import deepcopy, copy
import random


# TODO: add comments to explain functionality
# TODO: tidy repetitive statements if possible

def location2index(loc: str) -> tuple[int, ...]:
    '''converts chess location to corresponding x and y coordinates'''
    location = []
    newloc = []
    for x in loc:
        if not x.isnumeric():
            x = ord(x) - 96
            int(x)
            location.append(x)
        else:
            int(x)
            newloc.append(x)
    newloc = int(str("".join(newloc)))
    location.append(newloc)
    return tuple(location)


def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    offset = ord("a") - 1
    X = str(chr(x + offset))
    Y = str(y)
    letters = [X, Y]
    return "".join(letters)


class Piece:
    pos_X: int
    pos_Y: int
    side_: bool  # True for White and False for Black)

    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values'''
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_

    def __eq__(self, other):
        return self.pos_X == other.pos_X and self.pos_Y == other.pos_Y and self.side_ == other.side_

    def can_reach(self, pos_X, pos_Y, B):
        pass

    def can_move_to(self, pos_X, pos_Y, B):
        pass

    def move_to(self, pos_X, pos_Y, B):
        pass


Board = tuple[int, list[Piece]]


def is_piece_at(pos_X: int, pos_Y: int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B'''
    true_is_piece_at = 0
    for i in B[1]:
        if i.pos_X == pos_X and i.pos_Y == pos_Y:
            true_is_piece_at += 1
        else:
            pass
    if true_is_piece_at != 0:
        return True
    else:
        return False


def piece_at(pos_X: int, pos_Y: int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    for i in B[1]:
        if i.pos_X == pos_X and i.pos_Y == pos_Y:
            return i
        else:
            pass



class Rook(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule2] and [Rule4](see section Intro)
        Hint: use is_piece_at
        '''
        if is_piece_at(pos_X, pos_Y, B) == True and piece_at(pos_X, pos_Y, B).side_ == self.side_ \
                or (pos_X > B[0]) or (pos_Y > B[0]):
            return False
        else:
            if pos_X == self.pos_X or pos_Y == self.pos_Y:
                path_clear = True
                if pos_X == self.pos_X:
                    for y in range(self.pos_Y + 1, pos_Y):
                        if is_piece_at(self.pos_X, y, B):
                            path_clear = False
                            break
                    for y in range(self.pos_Y - 1, pos_Y, -1):
                        if is_piece_at(self.pos_X, y, B):
                            path_clear = False
                            break
                else:
                    for x in range(self.pos_X + 1, pos_X):
                        if is_piece_at(x, self.pos_Y, B):
                            path_clear = False
                            break
                    for x in range(self.pos_X - 1, pos_X, -1):
                        if is_piece_at(x, self.pos_Y, B):
                            path_clear = False
                            break

                if path_clear:
                    return True
                else:
                    return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to all chess rules
        
        Hints:
        - firstly, check [Rule2] and [Rule4] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule5], use is_check on new board
        '''
        new_B = deepcopy(B)
        if self.can_reach(pos_X, pos_Y, B):
            if is_piece_at(pos_X, pos_Y, B):
                new_B[1].remove(piece_at(pos_X, pos_Y, new_B))
                new_P = Rook(pos_X, pos_Y, self.side_)
                new_B[1].remove(piece_at(self.pos_X, self.pos_Y, new_B))
                new_B[1].append(new_P)
            else:
                new_P = Rook(pos_X, pos_Y, self.side_)
                new_B[1].remove(piece_at(self.pos_X, self.pos_Y, new_B))
                new_B[1].append(new_P)
            if is_check(self.side_, new_B):
                return False
            else:
                return True
        else:
            return False

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
            returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B
            assumes this move is valid according to chess rules
            '''
        if is_piece_at(pos_X, pos_Y, B):
            B[1].remove(piece_at(pos_X, pos_Y, B))
            self.pos_X = pos_X
            self.pos_Y = pos_Y
        else:
            self.pos_X = pos_X
            self.pos_Y = pos_Y
        return B


class Bishop(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''
        x = abs(self.pos_X - pos_X)
        y = abs(self.pos_Y - pos_Y)
        if is_piece_at(pos_X, pos_Y, B) == True and piece_at(pos_X, pos_Y, B).side_ == self.side_ \
                or (pos_X > B[0]) or (pos_Y > B[0]):
            return False
        else:
            path_clear = True
            for i in range(1, x):
                if is_piece_at(self.pos_X + i, self.pos_Y + i, B):
                    path_clear = False
                    break
                elif is_piece_at(self.pos_X - i, self.pos_Y - i, B):
                    path_clear = False
                    break
                elif is_piece_at(self.pos_X + i, self.pos_Y - i, B):
                    path_clear = False
                    break
                elif is_piece_at(self.pos_X - i, self.pos_Y + i, B):
                    path_clear = False
                    break
                else:
                    pass
            if path_clear and x == y:
                return True
            else:
                return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        new_B = deepcopy(B)
        if self.can_reach(pos_X, pos_Y, B):
            if is_piece_at(pos_X, pos_Y, B):
                new_B[1].remove(piece_at(pos_X, pos_Y, new_B))
                new_P = Bishop(pos_X, pos_Y, self.side_)
                new_B[1].remove(piece_at(self.pos_X, self.pos_Y, new_B))
                new_B[1].append(new_P)
            else:
                new_P = Bishop(pos_X, pos_Y, self.side_)
                new_B[1].remove(piece_at(self.pos_X, self.pos_Y, new_B))
                new_B[1].append(new_P)
            if is_check(self.side_, new_B):
                return False
            else:
                return True
        else:
            return False
    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''
        if is_piece_at(pos_X, pos_Y, B):
            B[1].remove(piece_at(pos_X, pos_Y, B))
            self.pos_X = pos_X
            self.pos_Y = pos_Y
        else:
            self.pos_X = pos_X
            self.pos_Y = pos_Y
        return B


class King(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''
        if is_piece_at(pos_X, pos_Y, B) == True and piece_at(pos_X, pos_Y, B).side_ == self.side_:
            return False
        if abs(self.pos_X - pos_X) < 2 and abs(self.pos_Y - pos_Y) < 2 and \
                (pos_X, pos_Y != self.pos_X, self.pos_Y) and (pos_X < B[0]) and (pos_Y < B[0]):
            return True
        else:
            return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        new_B = deepcopy(B)
        if self.can_reach(pos_X, pos_Y, B):
            if is_piece_at(pos_X, pos_Y, B):
                new_B[1].remove(piece_at(pos_X, pos_Y, new_B))
                new_P = King(pos_X, pos_Y, self.side_)
                new_B[1].remove(piece_at(self.pos_X, self.pos_Y, new_B))
                new_B[1].append(new_P)
            else:
                new_P = King(pos_X, pos_Y, self.side_)
                new_B[1].remove(piece_at(self.pos_X, self.pos_Y, new_B))
                new_B[1].append(new_P)
            if is_check(self.side_, new_B):
                return False
            else:
                return True
        else:
            return False
    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        if is_piece_at(pos_X, pos_Y, B):
            B[1].remove(piece_at(pos_X, pos_Y, B))
            self.pos_X = pos_X
            self.pos_Y = pos_Y
        else:
            self.pos_X = pos_X
            self.pos_Y = pos_Y
        return B


def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''
    king_x = 0
    king_y = 0
    check = None
    for j in B[1]:
        if side == j.side_ and type(j) == King:
            king_x = j.pos_X
            king_y = j.pos_Y
    for k in B[1]:
        if k.side_ != side and k.can_reach(king_x, king_y, B):
            check = True
            break
        else:
            check = False
    return check


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_reach 
    '''
    board = []
    side_moves = []
    for i in range(1, B[0] + 1):
        for j in range(1, B[0] + 1):
            board.append((i, j))
    for i in B[1]:
        for j in board:
            temp_board = deepcopy(B)
            if i.side_ == side and i.can_reach(j[0], j[1], B):
                if is_piece_at(j[0], j[1], B):
                    temp_board[1].remove(piece_at(j[0], j[1], B))
                    new_P = i.__class__(j[0], j[1], i.side_)
                    temp_board[1].remove(i)
                    temp_board[1].append(new_P)
                else:
                    new_P = i.__class__(j[0], j[1], i.side_)
                    temp_board[1].remove(i)
                    temp_board[1].append(new_P)
                if not is_check(side, temp_board):
                    side_moves.append([i, j])
    if side_moves == []:
        return True
    else:
        return False


def create_piece(code: str, x: int, y: int, side: bool) -> Piece:
    piece_codes = {'B': Bishop, 'K': King, 'R': Rook}
    return piece_codes[code](x, y, side)


def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    white_pieces_final = []
    black_pieces_final = []
    with open(filename, "r") as fl:
        lines = fl.readlines()

        white_pieces = lines[1].rstrip().split(",")
        white_pieces = [s.strip() for s in white_pieces]
        white_pieces_locations = [location2index(piece[1:]) for piece in white_pieces]
        for i in zip(white_pieces, white_pieces_locations):
            white_pieces_final.append(create_piece(i[0][0], i[1][0], i[1][1], True))

        black_pieces = lines[2].rstrip().split(",")
        black_pieces = [s.strip() for s in black_pieces]
        black_pieces_locations = [location2index(piece[1:]) for piece in black_pieces]
        for i in zip(black_pieces, black_pieces_locations):
            black_pieces_final.append(create_piece(i[0][0], i[1][0], i[1][1], False))

        fl.close()
    pieces = white_pieces_final + black_pieces_final
    pieces_locations = white_pieces_locations + black_pieces_locations

    B = (int(lines[0].rstrip()), pieces)
    pieces_over = []
    [pieces_over.append(x) for x in pieces_locations if x[0] > B[0] or x[1] > B[0]]
    if len(set(pieces_locations)) < len(pieces):
        raise IOError
    elif len(lines[0].rstrip().split()) > 1:
        raise IOError
    elif pieces_over != []:
        raise IOError
    else:
        return B


def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''
    piece_codes = {King: 'K', Bishop: 'B', Rook: 'R'}
    size = str(B[0])
    white_pieces = []
    black_pieces = []
    for piece in B[1]:
        if piece.side_:
            x = piece.pos_X
            y = piece.pos_Y
            code = piece_codes[piece.__class__]
            white_pieces.append(str(code) + index2location(x, y))
        else:
            x = piece.pos_X
            y = piece.pos_Y
            code = piece_codes[piece.__class__]
            black_pieces.append(str(code) + index2location(x, y))
    white_pieces = ','.join(white_pieces)
    black_pieces = ','.join(black_pieces)
    with open(filename, "w") as fl:
        fl.write(size + "\n")
        fl.write(white_pieces + "\n")
        fl.write(black_pieces + "\n")
        fl.close()


def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''
    board = []
    possible_moves = []
    for i in range(1, B[0] + 1):
        for j in range(1, B[0] + 1):
            board.append((i, j))
    for piece in B[1]:
        for j in board:
            temp_board = deepcopy(B)
            if piece.side_ == False and piece.can_reach(j[0], j[1], B):
                if is_piece_at(j[0], j[1], B):
                    temp_board[1].remove(piece_at(j[0], j[1], B))
                    new_P = piece.__class__(j[0], j[1], piece.side_)
                    temp_board[1].remove(piece)
                    temp_board[1].append(new_P)
                else:
                    new_P = piece.__class__(j[0], j[1], piece.side_)
                    temp_board[1].remove(piece)
                    temp_board[1].append(new_P)
                if is_check(False, temp_board) == False:
                    possible_moves.append((piece, j[0], j[1]))
    black_move = random.choice(possible_moves)
    return black_move


def conf2unicode(B: Board) -> str:
    '''converts board configuration B to unicode format string (see section Unicode board configurations)'''
    piece_codes_white = {King: "♔", Bishop: "♗", Rook: "♖"}
    piece_codes_black = {King: "♚", Rook: "♜", Bishop: "♝"}
    unicode_board = []
    for i in range(1, B[0] + 1):
        for j in range(1, B[0] + 1):
            unicode_board.append((i, j))
    for piece in B[1]:
        for i in range(len(unicode_board)):
            if piece.side_:
                if piece.pos_Y == unicode_board[i][0] and piece.pos_X == unicode_board[i][1]:
                    unicode_board[i] = piece_codes_white[piece.__class__]
                    break
            elif piece.side_ == False:
                if piece.pos_Y == unicode_board[i][0] and piece.pos_X == unicode_board[i][1]:
                    unicode_board[i] = piece_codes_black[piece.__class__]
                    break
    for x in range(len(unicode_board)):
        if isinstance(unicode_board[x], tuple):
            unicode_board[x] = "\u2001"
        str.strip(unicode_board[x])
    unicode_board = [unicode_board[x:x + B[0]] for x in range(0, len(unicode_board), B[0])]
    unicode_board.reverse()
    for x in range(len(unicode_board)):
        unicode_board[x].append("\n")
        unicode_board[x] = ''.join(unicode_board[x])
    unicode_board_fn = ''.join(unicode_board)
    unicode_board_fn = unicode_board_fn[:-1]

    return unicode_board_fn


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''
    while True:
        try:
            filename = input("File name for initial configuration: ")
            b = read_board(filename)
            break
        except IOError:
            if filename == "QUIT":
                quit()
            else:
                print("This is not a valid file.")
    print(conf2unicode(b))
    while True:
        try:
            next_move = input("Next move of white:")
            piece_selected_loc = location2index(next_move[:2])
            new_location = location2index(next_move[-2:])
            piece_selected = piece_at(piece_selected_loc[0], piece_selected_loc[1], b)
            if piece_selected.can_move_to(new_location[0], new_location[1], b):
                piece_selected.move_to(new_location[0], new_location[1], b)
                print("The configuration after White's move is:")
                print(conf2unicode(b))
                if is_checkmate(False, b):
                    print("Game over. White wins.")
                    quit()
                else:
                    black_move = find_black_move(b)
                    black_piece_selected = index2location(black_move[0].pos_X, black_move[0].pos_Y)
                    black_new_location = black_piece_selected + index2location(black_move[1], black_move[2])
                    black_move[0].move_to(black_move[1], black_move[2], b)
                    print(
                        "Next move of Black is {}. The configuration after Black's move is:".format(black_new_location))
                    print(conf2unicode(b))
                    if is_checkmate(True, b):
                        print("Game over. Black wins.")
                        quit()
                    else:
                        pass
            else:
                raise ValueError
        except ValueError:
            if next_move == "QUIT":
                save_location = input("File name to store the configuration:")
                save_board(save_location, b)
                print("The game configuration saved.")
                quit()
            else:
                print("This is not a valid move.")


if __name__ == '__main__':  # keep this in
    main()
