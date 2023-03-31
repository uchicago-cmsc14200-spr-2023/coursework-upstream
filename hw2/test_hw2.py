from hw2 import *
from trees import *

BST = Union[BSTEmpty, BSTNode]

def test_task1_1() -> None:
    b = Boolean(True)
    assert b.is_const()
    assert b.num_nodes() == 1
    assert b.eval()
    assert str(b) == "True"

def test_task1_2() -> None:
    b = Boolean(False)
    assert b.is_const()
    assert b.num_nodes() == 1
    assert not b.eval()
    assert str(b) == "False"

def test_task1_3() -> None:
    b1 = Boolean(True)
    b2 = Boolean(True)
    op = And(b1, b2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert op.eval()

def test_task1_4() -> None:
    b1 = Boolean(True)
    b2 = Boolean(False)
    op = And(b1, b2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert not op.eval()

def test_task1_5() -> None:
    b1 = Boolean(False)
    b2 = Boolean(True)
    op = And(b1, b2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert not op.eval()

def test_task1_6() -> None:
    b1 = Boolean(False)
    b2 = Boolean(False)
    op = And(b1, b2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert not op.eval()

def test_task1_7() -> None:
    b1 = Boolean(True)
    b2 = Boolean(True)
    op = Or(b1, b2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert op.eval()

def test_task1_8() -> None:
    b1 = Boolean(True)
    b2 = Boolean(False)
    op = Or(b1, b2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert op.eval()

def test_task1_9() -> None:
    b1 = Boolean(False)
    b2 = Boolean(True)
    op = Or(b1, b2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert op.eval()

def test_task1_10() -> None:
    b1 = Boolean(False)
    b2 = Boolean(False)
    op = Or(b1, b2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert not op.eval()

def test_task1_11() -> None:
    b = Boolean(True)
    op = Not(b)
    assert not op.is_const()
    assert op.num_nodes() == 2
    assert not op.eval()

def test_task1_12() -> None:
    b = Boolean(False)
    op = Not(b)
    assert not op.is_const()
    assert op.num_nodes() == 2
    assert op.eval()

def test_task1_13() -> None:
    b1 = Boolean(True)
    b2 = Boolean(True)
    op1 = Not(b1)
    op2 = Or(op1, b2)
    assert not op2.is_const()
    assert op2.num_nodes() == 4
    assert op2.eval()

def test_task1_14() -> None:
    b1 = Boolean(True)
    b2 = Boolean(True)
    b3 = Boolean(True)
    op1 = Not(b1)
    op2 = Or(b2, b3)
    op3 = And(op1, op2)
    assert not op3.is_const()
    assert op3.num_nodes() == 6
    assert not op3.eval()

def test_task1_15() -> None:
    b1 = Boolean(False)
    b2 = Boolean(False)
    b3 = Boolean(False)
    op1 = Not(b1)
    op2 = Or(b2, b3)
    op3 = And(op1, op2)
    op4 = Not(op3)
    assert not op4.is_const()
    assert op4.num_nodes() == 7
    assert op4.eval()

def test_task2_0() -> None:
    bst = BSTEmpty()
    assert verify_avl(bst)

def test_task2_1() -> None:
    values = [1]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert verify_avl(bst)

def test_task2_2() -> None:
    values = [1, 2]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert verify_avl(bst)

def test_task2_3() -> None:
    values = [2, 1]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert verify_avl(bst)

def test_task2_4() -> None:
    values = [2, 1, 3]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert verify_avl(bst)

def test_task2_5() -> None:
    values = [1, 2, 3]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert not verify_avl(bst)

def test_task2_6() -> None:
    values = [1, 3, 2]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert not verify_avl(bst)

def test_task2_7() -> None:
    values = [3, 2, 1]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert not verify_avl(bst)

def test_task2_8() -> None:
    values = [3, 1, 2]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert not verify_avl(bst)

def test_task2_9() -> None:
    values = [2, 1, 3, 4]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert verify_avl(bst)

def test_task2_10() -> None:
    values = [2, 1, 4, 3]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert verify_avl(bst)

def test_task2_11() -> None:
    values = [3, 4, 1, 2]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert verify_avl(bst)

def test_task2_12() -> None:
    values = [3, 4, 2, 1]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert verify_avl(bst)

def test_task2_13() -> None:
    values = [2, 1, 3, 4, 5]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert not verify_avl(bst)

def test_task2_14() -> None:
    values = [2, 1, 3, 4, 5, 0]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert not verify_avl(bst)

def test_task2_15() -> None:
    values = [5, 6, 1, 4, 3]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert not verify_avl(bst)

def test_task2_16() -> None:
    values = [5, 6, 1, 4, 3, 7]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert not verify_avl(bst)

def test_task3_1() -> None:
    bst = BSTNodeOpt(1, BSTEmptyOpt(), BSTEmptyOpt())
    assert bst.num_nodes == 1

def test_task3_2() -> None:
    n1 = BSTNodeOpt(2, BSTEmptyOpt(), BSTEmptyOpt())
    n2 = BSTNodeOpt(1, BSTEmptyOpt(), n1)
    assert n2.num_nodes == 2

def test_task3_3() -> None:
    n1 = BSTNodeOpt(1, BSTEmptyOpt(), BSTEmptyOpt())
    n2 = BSTNodeOpt(2, n1, BSTEmptyOpt())
    assert n2.num_nodes == 2

def test_task3_4() -> None:
    n1 = BSTNodeOpt(1, BSTEmptyOpt(), BSTEmptyOpt())
    n2 = BSTNodeOpt(3, BSTEmptyOpt(), BSTEmptyOpt())
    n3 = BSTNodeOpt(2, n1, n2)
    assert n3.num_nodes == 3

def test_task3_5() -> None:
    bst = BSTNodeOpt(1, BSTEmptyOpt(), BSTEmptyOpt())
    values = [2]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 2

def test_task3_6() -> None:
    bst = BSTNodeOpt(2, BSTEmptyOpt(), BSTEmptyOpt())
    values = [1]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 2

def test_task3_7() -> None:
    bst = BSTNodeOpt(2, BSTEmptyOpt(), BSTEmptyOpt())
    values = [1, 3]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 3

def test_task3_8() -> None:
    bst = BSTNodeOpt(3, BSTEmptyOpt(), BSTEmptyOpt())
    values = [4, 1, 2]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 4

def test_task3_9() -> None:
    bst = BSTNodeOpt(2, BSTEmptyOpt(), BSTEmptyOpt())
    values = [1, 3, 4]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 4
    
def test_task3_10() -> None:
    bst = BSTNodeOpt(4, BSTEmptyOpt(), BSTEmptyOpt())
    values = [2, 1, 3, 5]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 5

def test_task3_11() -> None:
    bst = BSTNodeOpt(4, BSTEmptyOpt(), BSTEmptyOpt())
    values = [2, 1, 3, 5, 6]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 6

def test_task3_12() -> None:
    bst = BSTNodeOpt(4, BSTEmptyOpt(), BSTEmptyOpt())
    values = [2, 1, 3, 6, 5, 8, 7, 9]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 9

def test_task3_13() -> None:
    bst = BSTNodeOpt(4, BSTEmptyOpt(), BSTEmptyOpt())
    values = [2, 1, 3, 6, 5, 8, 7, 9, 0]
    for v in values:
        bst = bst.insert(v)
    assert bst.num_nodes == 10

def test_task4_1() -> None:
    b = Board(1, 1)
    assert not b.is_full

def test_task4_2() -> None:
    b = Board(1, 1)
    b.add_piece("BLACK", (0, 0))
    assert b.is_full

def test_task4_3() -> None:
    b = Board(1, 2)
    assert not b.is_full

def test_task4_4() -> None:
    b = Board(1, 2)
    b.add_piece("BLACK", (0, 0))
    assert not b.is_full

def test_task4_5() -> None:
    b = Board(1, 2)
    b.add_piece("BLACK", (0, 1))
    assert not b.is_full

def test_task4_6() -> None:
    b = Board(1, 2)
    b.add_piece("BLACK", (0, 0))
    b.add_piece("BLACK", (0, 1))
    assert b.is_full

def test_task4_7() -> None:
    b = Board(2, 1)
    assert not b.is_full

def test_task4_8() -> None:
    b = Board(2, 1)
    b.add_piece("BLACK", (0, 0))
    assert not b.is_full

def test_task4_9() -> None:
    b = Board(2, 1)
    b.add_piece("BLACK", (1, 0))
    assert not b.is_full

def test_task4_10() -> None:
    b = Board(2, 1)
    b.add_piece("BLACK", (0, 0))
    b.add_piece("BLACK", (1, 0))
    assert b.is_full

def test_task4_11() -> None:
    b = Board(2, 2)
    assert not b.is_full

def test_task4_12() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (0, 0))
    assert not b.is_full

def test_task4_13() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (0, 1))
    assert not b.is_full

def test_task4_14() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (1, 0))
    assert not b.is_full

def test_task4_15() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (1, 1))
    assert not b.is_full

def test_task4_16() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (0, 0))
    b.add_piece("BLACK", (1, 1))
    assert not b.is_full

def test_task4_17() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (0, 0))
    b.add_piece("BLACK", (1, 0))
    assert not b.is_full

def test_task4_18() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (0, 0))
    b.add_piece("BLACK", (0, 1))
    assert not b.is_full

def test_task4_19() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (0, 0))
    b.add_piece("BLACK", (0, 1))
    b.add_piece("BLACK", (1, 0))
    assert not b.is_full

def test_task4_20() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (0, 1))
    b.add_piece("BLACK", (1, 0))
    b.add_piece("BLACK", (1, 1))
    assert not b.is_full

def test_task4_21() -> None:
    b = Board(2, 2)
    b.add_piece("BLACK", (0, 0))
    b.add_piece("BLACK", (0, 1))
    b.add_piece("BLACK", (1, 0))
    b.add_piece("BLACK", (1, 1))
    assert b.is_full

def has_duplicates(moves: List[Tuple[int,int]]) -> bool:
    return len(set(moves)) != len(moves)

def test_task5_1() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (0, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (2, 2) in moves

def test_task5_2() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (0, 1))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (2, 1) in moves

def test_task5_3() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (0, 2))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (2, 0) in moves

def test_task5_4() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (1, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (1, 2) in moves

def test_task5_5() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (1, 2))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (1, 0) in moves

def test_task5_6() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (2, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (0, 2) in moves

def test_task5_7() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (2, 1))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (0, 1) in moves

def test_task5_8() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (2, 2))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (0, 0) in moves

def test_task5_9() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("BLACK", (2, 1))
    b.add_piece("WHITE", (2, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 2
    assert (0, 2) in moves
    assert (2, 2) in moves

def test_task5_10() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("BLACK", (2, 1))
    b.add_piece("BLACK", (0, 0))
    b.add_piece("WHITE", (2, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 2
    assert (0, 2) in moves
    assert (2, 2) in moves

def test_task5_11() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("BLACK", (2, 1))
    b.add_piece("BLACK", (1, 0))
    b.add_piece("WHITE", (2, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 3
    assert (0, 0) in moves
    assert (0, 2) in moves
    assert (2, 2) in moves

def test_task5_12() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (0, 0))
    b.add_piece("BLACK", (1, 0))
    b.add_piece("BLACK", (2, 0))
    b.add_piece("WHITE", (0, 1))
    b.add_piece("WHITE", (1, 1))
    b.add_piece("WHITE", (2, 1))
    moves = get_moves(b, "BLACK")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 3
    assert (0, 2) in moves
    assert (1, 2) in moves
    assert (2, 2) in moves

def test_task5_13() -> None:
    b = Board(3, 3)
    b.add_piece("WHITE", (1, 1))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 0

def test_task5_14() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 2))
    b.add_piece("WHITE", (1, 1))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 0

def test_task5_15() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (0, 1))
    b.add_piece("WHITE", (1, 1))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 0

def test_task5_16() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (1, 0))
    b.add_piece("WHITE", (1, 2))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 0

def test_task5_17() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("BLACK", (1, 2))
    b.add_piece("WHITE", (1, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 0

def test_task5_18() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (1, 2))
    b.add_piece("WHITE", (2, 2))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 2
    assert (0, 0) in moves
    assert (1, 0) in moves

def test_task5_19() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (1, 1))
    b.add_piece("WHITE", (1, 2))
    b.add_piece("WHITE", (2, 2))
    b.add_piece("WHITE", (2, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 3
    assert (0, 0) in moves
    assert (1, 0) in moves
    assert (0, 2) in moves

def test_task5_20() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (2, 1))
    b.add_piece("WHITE", (1, 2))
    b.add_piece("WHITE", (2, 0))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (2, 2) in moves

def test_task5_21() -> None:
    b = Board(3, 3)
    b.add_piece("BLACK", (0, 2))
    b.add_piece("BLACK", (2, 1))
    b.add_piece("WHITE", (0, 0))
    b.add_piece("WHITE", (2, 2))
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 1
    assert (2, 0) in moves

def test_task5_22() -> None:
    b = Board(4, 6)
    for loc in [(0, 2), (1, 2), (2, 2), (2, 3), (3, 2), (3, 4)]:
        b.add_piece("WHITE", loc)
    for loc in [(0, 3), (1, 3), (2, 4)]:
        b.add_piece("BLACK", loc)
    moves = get_moves(b, "WHITE")
    assert not has_duplicates(moves), "Make sure you don't include duplicate moves!"
    assert len(moves) == 4
    assert (0, 4) in moves
    assert (1, 4) in moves
    assert (2, 5) in moves
    assert (3, 5) in moves





