from chess_puzzle import *


def test_location2index1():
    assert location2index("e2") == (5,2)

def test_location2index2():
    assert location2index("e12") == (5,12)

def test_location2index3():
    assert location2index("z26") == (26,26)

def test_index2location1():
    assert index2location(5,2) == "e2"

def test_index2location2():
    assert index2location(12,3) =="l3"

def test_index2location3():
    assert index2location(15,7) == "o7"

wb1 = Bishop(1,1,True)
wr1 = Rook(1,2,True)
wb2 = Bishop(5,2, True)
bk = King(2,3, False)
br1 = Rook(4,3,False)
br2 = Rook(2,4,False)
br3 = Rook(5,4, False)
wr2 = Rook(1,5, True)
wk = King(3,5, True)

B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
'''
♖ ♔  
 ♜  ♜
 ♚ ♜ 
♖   ♗
♗    
'''

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False

def test_is_piece_at2():
    assert is_piece_at(2,3,B1) == True

def test_is_piece_at3():
    assert is_piece_at(5,3, B1) == False

def test_piece_at1():
    assert piece_at(4,3, B1) == br1

def test_piece_at2():
    assert piece_at(1,5, B1) ==  wr2

def test_piece_at3():
    assert piece_at(5,4, B1) == br3

def test_piece_at4():
    assert piece_at(3,5, B1) == wk

def test_can_reach1():
    assert wr2.can_reach(4,5, B1) == False

def test_can_reach2():
    assert wr2.can_reach(1,2,B1) == False

def test_can_reach3():
    assert br1.can_reach(4,5,B1) == True

def test_can_reach4():
    assert br3.can_reach(1,4, B1) == False

def test_can_reach5():
    assert br3.can_reach(5,1,B1) == False

def test_can_reach6():
    assert br1.can_reach(1,3,B1) == False

def test_can_reach7():
    assert wr1.can_reach(3,2, B1) == True

def test_can_reach8():
    assert wb1.can_reach(4,4, B1) == True

def test_can_reach9():
    assert wb2.can_reach(4,3,B1) == True

def test_can_reach10():
    assert wb2.can_reach(3,4, B1) == False

def test_can_reach11():
    assert wk.can_reach(3,4,B1) == True

def test_can_reach12():
    assert wk.can_reach(2,4,B1) == True

def test_can_reach13():
    assert bk.can_reach(2,4,B1) == False

def test_can_reach14():
    wr2b = Rook(2, 5, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2b, wk])
    assert wr2b.can_reach(2,3,B2) == False

def test_can_reach15():
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
    assert wr2.can_reach(1,4,B1) == True

br2a = Rook(1,5,False)
wr2a = Rook(2,5,True)
bb1 = Bishop(2,1,False)

def test_can_move_to1():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wr2a.can_move_to(2,4, B2) == False

def test_can_move_to2():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert br2a.can_move_to(2, 4, B2) == False

def test_can_move_to3():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, bb1, wk])
    assert bb1.can_move_to(2, 4, B2) == False

def test_can_move_to4():
    wr1 = Rook(1,2,True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert bk.can_move_to(2, 2, B2) == False

def test_can_move_to5():
    wr2 = Rook(3,3,True)
    br2a = Rook(3,1, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wr2, wk])
    assert wr2.can_move_to(2,3,B2) == False

def test_can_move_to6():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wb1.can_move_to(2,2,B2) == True

def test_is_check1():
    wr2b = Rook(2,4,True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True

def test_is_check2():
    wb2a = Bishop(4, 1, True)
    wr2b = Rook(4, 4, True)
    B2 = (5, [wb1, wr1, wb2a, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True

def test_is_check3():
    br1 = Rook(4,5,False)
    wr2b = Rook(4, 4, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True,B2) == True

def test_is_check4():
    br3 = Rook(5,5, False)
    wr2b = Rook(4, 4, True)
    wr1 = Rook(2,2, True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(False, B2) == True

def test_is_check5():
    wr2b = Rook(2,5,True)
    wb2  = Bishop(5,2,True)
    wb1 = Bishop(1,1,True)
    bk = King(2, 3, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2b, wk])
    assert is_check(False, B2) == False

def test_is_check6():
    bk = King(2,2,False)
    wr1 = Rook(1,2,True)
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
    assert is_check(True,B1) == False

def test_is_checkmate1():
    br2b = Rook(4,5,False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr2, wk])
    assert is_checkmate(True, B2) == True

def test_is_checkmate2():
    br2b = Rook(2, 2, False)
    br1a = Rook(5,5, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1a, br2b, br3, wr2, wk])
    assert is_checkmate(True, B2) == True

wr2c = Rook(1, 5, True)

def test_is_checkmate3():
    wr1a = Rook(4, 3, True)
    br2b = Rook(2, 4, False)
    wb2 = Bishop(4, 1, True)
    wr2c = Rook(1, 5, True)
    wb1 = Bishop(1, 1, True)
    wr3 = Rook(4,4, True)

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
    assert wb2.move_to(4,3,B1) == (5, [wb1, wr1, wb2, bk, br2, br3, wr2, wk])


def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_conf2unicode1():
    assert conf2unicode(B1) == "♖ ♔  \n ♜  ♜\n ♚ ♜ \n♖   ♗\n♗    "

