import pytest

from chess_puzzle import *


def test_location2index1():
    assert location2index("e2") == (5, 2)


def test_location2index2():
    assert location2index("e12") == (5, 12)


def test_location2index3():
    assert location2index("z26") == (26, 26)


# testing that uppercase letters are converted to lower
def test_location2index4():
    assert location2index("Z24") == (26, 24)


# exception raised
def test_location2index5():
    with pytest.raises(Exception) as exception:
        assert location2index("z27") == exception


def test_index2location1():
    assert index2location(5, 2) == "e2"


def test_index2location2():
    assert index2location(12, 3) == "l3"


def test_index2location3():
    assert index2location(15, 7) == "o7"


def test_index2location4():
    assert index2location(26, 26) == "z26"


def test_index2location5():
    assert index2location(17, 24) == "q24"


wb1 = Bishop(1, 1, True)
wr1 = Rook(1, 2, True)
wb2 = Bishop(5, 2, True)
bk = King(2, 3, False)
br1 = Rook(4, 3, False)
br2 = Rook(2, 4, False)
br3 = Rook(5, 4, False)
wr2 = Rook(1, 5, True)
wk = King(3, 5, True)

B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
'''
♖ ♔  
 ♜  ♜
 ♚ ♜ 
♖   ♗
♗    
'''


def test_is_piece_at1():
    assert is_piece_at(2, 2, B1) == False


def test_is_piece_at2():
    assert is_piece_at(2, 3, B1) == True


def test_is_piece_at3():
    assert is_piece_at(5, 3, B1) == False


# out of board size
def test_is_piece_at4():
    assert is_piece_at(6, 5, B1) == False


def test_is_piece_at5():
    assert is_piece_at(0, 5, B1) == False


def test_piece_at1():
    assert piece_at(4, 3, B1) == br1


def test_piece_at2():
    assert piece_at(1, 5, B1) == wr2


def test_piece_at3():
    assert piece_at(5, 4, B1) == br3


def test_piece_at4():
    assert piece_at(3, 5, B1) == wk


def test_piece_at5():
    assert piece_at(0, 5, B1) == None


# testing for rook
def test_can_reach1():
    assert wr2.can_reach(4, 5, B1) == False


def test_can_reach2():
    assert wr2.can_reach(1, 2, B1) == False


def test_can_reach3():
    assert br1.can_reach(4, 5, B1) == True


def test_can_reach4():
    assert br3.can_reach(1, 4, B1) == False


def test_can_reach5():
    assert br3.can_reach(5, 1, B1) == False


def test_can_reach6():
    assert br1.can_reach(1, 3, B1) == False


def test_can_reach7():
    assert wr1.can_reach(3, 2, B1) == True


# testing for bishop
# forwards and up
def test_can_reach8():
    assert wb1.can_reach(4, 4, B1) == True


def test_can_reach9():
    assert wb2.can_reach(4, 3, B1) == True


# forwards and down
def test_can_reach10():
    wb2 = Bishop(3, 3, True)
    assert wb2.can_reach(5, 1, B1) == True


# backwards and up
def test_can_reach11():
    bb = Bishop(5, 1, False)
    B1 = (5, [wb1, wr1, bb, bk, br1, br2, br3, wr2, wk])
    assert bb.can_reach(4, 2, B1) == True


# backwards and down
def test_can_reach12():
    bb = Bishop(5, 3, False)
    B1 = (5, [wb1, wr1, bb, bk, br1, br2, br3, wr2, wk])
    assert bb.can_reach(3, 1, B1) == True


# testing king in all directions
# down
def test_can_reach13():
    assert wk.can_reach(3, 4, B1) == True


# down left
def test_can_reach14():
    assert wk.can_reach(2, 4, B1) == True


# down right
def test_can_reach14a():
    assert wk.can_reach(4, 4, B1) == True


# up (piece of same side in way)
def test_can_reach15():
    assert bk.can_reach(2, 4, B1) == False


# up
def test_can_reach16():
    bk = King(3, 3, False)
    assert bk.can_reach(3, 4, B1) == True


# up and right
def test_can_reach17():
    bk = King(3, 3, False)
    assert bk.can_reach(4, 4, B1) == True


# up and left
def test_can_reach18():
    bk = King(4, 3, False)
    br1 = Rook(5, 3, False)
    assert bk.can_reach(3, 4, B1) == True


# left
def test_can_reach19():
    wk = King(3, 5, True)
    assert wk.can_reach(4, 5, B1) == True


# right
def test_can_reach19a():
    assert wk.can_reach(2, 5, B1) == True


br2a = Rook(1, 5, False)
wr2a = Rook(2, 5, True)
bb1 = Bishop(2, 1, False)


def test_can_reach19b():
    wr1 = Rook(2, 2, True)
    wb1 = Bishop(1, 1, True)
    B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
    assert wb1.can_reach(5, 5, B1) == False


def test_can_move_to1():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wr2a.can_move_to(2, 4, B2) == False


# piece of same side in path
def test_can_move_to2():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert br2a.can_move_to(2, 4, B2) == False


# incorrect movement
def test_can_move_to3():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, bb1, wk])
    assert bb1.can_move_to(2, 4, B2) == False


# put self in check
def test_can_move_to4():
    wr1 = Rook(1, 2, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert bk.can_move_to(2, 2, B2) == False


# puts king in check
def test_can_move_to5():
    wr2 = Rook(3, 3, True)
    br2a = Rook(3, 1, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wr2, wk])
    assert wr2.can_move_to(2, 3, B2) == False


# can move without causing check
def test_can_move_to6():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wb1.can_move_to(2, 2, B2) == True


def test_is_check1():
    wr2b = Rook(2, 4, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True


def test_is_check2():
    wb2a = Bishop(4, 1, True)
    wr2b = Rook(4, 4, True)
    B2 = (5, [wb1, wr1, wb2a, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True


def test_is_check3():
    br1 = Rook(4, 5, False)
    wr2b = Rook(4, 4, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True


def test_is_check4():
    br3 = Rook(5, 5, False)
    wr2b = Rook(4, 4, True)
    wr1 = Rook(2, 2, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(False, B2) == True


def test_is_check5():
    wr2b = Rook(2, 5, True)
    wb2 = Bishop(5, 2, True)
    wb1 = Bishop(1, 1, True)
    bk = King(2, 3, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2b, wk])
    assert is_check(False, B2) == False


def test_is_check6():
    bk = King(2, 2, False)
    wr1 = Rook(1, 2, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert is_check(False, B2) == True


def test_is_check7():
    wb1 = Bishop(1, 1, True)
    wr1 = Rook(1, 2, True)
    wb2 = Bishop(5, 2, True)
    bk = King(2, 3, False)
    br1 = Rook(4, 3, False)
    br2 = Rook(2, 4, False)
    br3 = Rook(5, 4, False)
    wr2 = Rook(1, 5, True)
    wk = King(3, 5, True)

    B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
    assert is_check(True, B1) == False


def test_is_checkmate1():
    br2b = Rook(4, 5, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr2, wk])
    assert is_checkmate(True, B2) == True


# piece in the way of possible move out of check
def test_is_checkmate2():
    wb1 = Bishop(1, 1, True)
    wr1 = Rook(2, 2, True)
    wb2 = Bishop(5, 2, True)
    bk = King(2, 3, False)
    br1 = Rook(4, 3, False)
    br2 = Rook(5, 5, False)
    br3 = Rook(5, 4, False)
    wr2 = Rook(1, 5, True)
    wk = King(3, 5, True)

    B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
    assert is_checkmate(True, B1) == True


wr2c = Rook(1, 5, True)


def test_is_checkmate3():
    wr1a = Rook(4, 3, True)
    br2b = Rook(2, 4, False)
    wb2 = Bishop(4, 1, True)
    wr2c = Rook(1, 5, True)
    wb1 = Bishop(1, 1, True)
    wr3 = Rook(4, 4, True)

    B2 = (5, [wb1, wr1a, wb2, bk, br2b, br3, wr2c, wk, wr3])
    assert is_checkmate(False, B2) == True


def test_is_checkmate4():
    wb1 = Bishop(1, 1, True)
    wr1 = Rook(1, 2, True)
    wb2 = Bishop(5, 2, True)
    bk = King(2, 3, False)
    br1 = Rook(4, 3, False)
    br2 = Rook(2, 4, False)
    br3 = Rook(5, 4, False)
    wr2 = Rook(1, 5, True)
    wk = King(3, 5, True)

    B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
    assert is_checkmate(True, B1) == False


# available move by other piece to remove check
def test_is_checkmate5():
    wb1 = Bishop(1, 1, True)
    wr1 = Rook(1, 2, True)
    wb2 = Bishop(5, 2, True)
    bk = King(2, 3, False)
    br1 = Rook(4, 3, False)
    br2 = Rook(5, 5, False)
    br3 = Rook(5, 4, False)
    wr2 = Rook(1, 5, True)
    wk = King(3, 5, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
    assert is_checkmate(True, B2) == False

# piece taken in move (br1)
def test_move_to1():
    wb1 = Bishop(1, 1, True)
    wr1 = Rook(1, 2, True)
    wb2 = Bishop(5, 2, True)
    bk = King(2, 3, False)
    br1 = Rook(4, 3, False)
    br2 = Rook(2, 4, False)
    br3 = Rook(5, 4, False)
    wr2 = Rook(1, 5, True)
    wk = King(3, 5, True)

    B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
    assert wb2.move_to(4, 3, B1) == (5, [wb1, wr1, wb2, bk, br2, br3, wr2, wk])


b2_wk = King(1, 6, True)
b2_wb = Bishop(5, 2, True)
b2_wr = Rook(1, 5, True)
b2_wb2 = Bishop(6, 6, True)
b2_bk = King(2, 3, False)
b2_br = Rook(4, 6, False)
b2_br2 = Rook(6, 1, False)
b2_bb = Bishop(5, 4, False)

B2_board = (6, [b2_wk, b2_wb, b2_wr, b2_wb2, b2_bk, b2_br, b2_br2, b2_bb])
def test_move_to2():
    b2_br.move_to(6,6,B2_board)
    assert b2_br2.pos_X == 6

def test_move_to3():
    b2_wk.move_to(2,5,B2_board)
    assert b2_wk.pos_X == 2 and b2_wk.pos_Y == 5

def test_move_to4():
    b2_bb.move_to(5, 2, B2_board)
    assert b2_bb.pos_X == 5 and b2_bb.pos_Y == 2

def test_move_to5():
    b2_wb2.move_to(4,4,B2_board)
    assert b2_wb2.pos_Y == 4

b3_wk = King(1, 6, True)
b3_wb = Bishop(5, 2, True)
b3_wr = Rook(1, 5, True)
b3_wb2 = Bishop(6, 6, True)
b3_bk = King(2, 3, False)
b3_br = Rook(4, 6, False)
b3_br2 = Rook(6, 1, False)
b3_bb = Bishop(5, 4, False)

B3_board = (6, [b3_wk, b3_wb, b3_wr, b3_wb2, b3_bk, b3_br, b3_br2, b3_bb])

def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  # we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side_ == piece1.side_ and type(
                    piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]:  # we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side_ == piece1.side_ and type(
                    piece) == type(piece1):
                found = True
        assert found

def test_read_board2():
    B = read_board("board_examp3")
    assert B[0] == 6

    for piece in B[1]:
        found = False
        for piece1 in B3_board[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side_ == piece1.side_ and type(
                    piece) == type(piece1):
                found = True
        assert found

    for piece1 in B3_board[1]:
        found = False
        for piece in B[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side_ == piece1.side_ and type(
                    piece) == type(piece1):
                found = True
        assert found

b4_wk = King(1,1,True)
b4_wb = Bishop(2,3,True)
b4_wr = Rook(3,2,True)
b4_bk = King(2,2,False)
b4_br = Rook(3,3,False)

b4 = (3, [b4_wk,b4_wb,b4_wr,b4_bk,b4_br])

def test_read_board3():
    B = read_board("board_examp4")
    assert B[0] == 3

    for piece in B[1]:
        found = False
        for piece1 in b4[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side_ == piece1.side_ and type(
                    piece) == type(piece1):
                found = True
        assert found

    for piece1 in b4[1]:
        found = False
        for piece in B[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side_ == piece1.side_ and type(
                    piece) == type(piece1):
                found = True
        assert found

b5_wk = King(1,1,True)
b5_wb = Bishop(1,2,True)
b5_bk = King(2,1,False)

b5 = (2,[b5_wk,b5_wb,b5_bk])


def test_read_board4():
    B = read_board("board_examp5")
    assert B[0] == 2

    for piece in B[1]:
        found = False
        for piece1 in b5[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side_ == piece1.side_ and type(
                    piece) == type(piece1):
                found = True
        assert found

    for piece1 in b5[1]:
        found = False
        for piece in B[1]:
            if piece.pos_X == piece1.pos_X and piece.pos_Y == piece1.pos_Y and piece.side_ == piece1.side_ and type(
                    piece) == type(piece1):
                found = True
        assert found

def test_read_board5():
    with pytest.raises(IOError) as er:
        assert read_board("board_examp6") == er

def test_conf2unicode1():
    assert conf2unicode(B1) == "♖ ♔  \n ♜  ♜\n ♚ ♜ \n♖   ♗\n♗    "

def test_conf2unicode2():
    assert conf2unicode(B3_board) == "♔  ♜ ♗\n♖     \n    ♝ \n ♚    \n    ♗ \n     ♜"

def test_conf2unicode3():
    assert conf2unicode(b4) == " ♗♜\n ♚♖\n♔  "

def test_conf2unicode4():
    assert conf2unicode(b5) == "♗ \n♔♚"

b6_wk = King(1,2,True)
b6_wb = Rook(3,2,True)
b6_bk = King(3,3,True)

b6 = (7,[b6_bk,b6_wk,b6_wb])

def test_conf2unicode5():
    assert conf2unicode(b6)== "       \n       \n       \n       \n  ♔    \n♔ ♖    \n       "
