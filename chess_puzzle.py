def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
    location = []
    newloc = []
    for x in loc:
        if x.isnumeric() == False:
            x = ord(x) - 96
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
    return ("".join(letters))


class Piece:
    pos_X: int
    pos_Y: int
    side_: bool  # True for White and False for Black)

    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values'''
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_


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
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule2] and [Rule4](see section Intro)
        Hint: use is_piece_at
        '''
        if is_piece_at(pos_X, pos_Y, B) == True and piece_at(pos_X, pos_Y, B).side_ == self.side_:
            return False
        else:
            x = bool
            for i, j in zip(range(self.pos_X, pos_X-1), range(self.pos_Y, pos_Y-1)):
                if is_piece_at(i, j, B):
                    x = True
                else:
                    x = False
            if pos_X == self.pos_X or pos_Y == self.pos_Y and x == False:
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

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''


class Bishop(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''


class King(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''


def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_reach 
    '''


def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''


def save_board(filename: str) -> None:
    '''saves board configuration into file in current directory in plain format'''


def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''


def conf2unicode(B: Board) -> str:
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''


if __name__ == '__main__':  # keep this in
    main()
