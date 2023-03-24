from hw1 import *
from tree import TreeNode
from math import pi

def test_task1_1() -> None:
    words = ["hello"]
    letter = "h"

    assert words_that_start_with(words, letter) == 1

def test_task1_2() -> None:
    words = ["hello", "hi"]
    letter = "h"

    assert words_that_start_with(words, letter) == 2

def test_task1_3() -> None:
    words = ["hello", "bye"]
    letter = "h"

    assert words_that_start_with(words, letter) == 1

def test_task1_4() -> None:
    words = ["bye", "hello"]
    letter = "h"

    assert words_that_start_with(words, letter) == 1

def test_task1_5() -> None:
    words = ["bye", "hello", "goodbye"]
    letter = "h"

    assert words_that_start_with(words, letter) == 1

def test_task1_6() -> None:
    words = ["bye", "hello", "hi"]
    letter = "h"

    assert words_that_start_with(words, letter) == 2

def test_task1_7() -> None:
    words = ["hi", "hello", "bye"]
    letter = "h"

    assert words_that_start_with(words, letter) == 2

def test_task1_8() -> None:
    words = ["hi", "bye", "hello", "hola"]
    letter = "h"

    assert words_that_start_with(words, letter) == 3

def test_task1_9() -> None:
    words = ["hi", "bye", "hello", "goodbye", "hola"]
    letter = "b"

    assert words_that_start_with(words, letter) == 1

def test_task1_10() -> None:
    words = ["hbi", "hellob", "goodbye", "hola"]
    letter = "b"

    assert words_that_start_with(words, letter) == 0

def test_task1_11() -> None:
    words: List[str] = []
    letter = "b"

    assert words_that_start_with(words, letter) == 0

def test_task1_12() -> None:
    words = ["hello"]
    letter = "b"

    assert words_that_start_with(words, letter) == 0

def test_task1_13() -> None:
    words = ["hello"]
    letter = "H"

    assert words_that_start_with(words, letter) == 0

def test_task1_14()  -> None:
    words = ["Hello"]
    letter = "h"

    assert words_that_start_with(words, letter) == 0

def test_task3_1()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(0)
    n1.add_child(n2)

    assert num_repeated_ancestors(n1) == 1

def test_task3_2()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n1.add_child(n2)

    assert num_repeated_ancestors(n1) == 0

def test_task3_3()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n1.add_child(n2)
    n1.add_child(n3)

    assert num_repeated_ancestors(n1) == 0

def test_task3_4()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(1)
    n1.add_child(n2)
    n1.add_child(n3)

    assert num_repeated_ancestors(n1) == 0

def test_task3_5()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(0)
    n3 = TreeNode(0)
    n1.add_child(n2)
    n1.add_child(n3)

    assert num_repeated_ancestors(n1) == 2

def test_task3_6()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(0)
    n1.add_child(n2)
    n1.add_child(n3)

    assert num_repeated_ancestors(n1) == 1

def test_task3_7()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(0)
    n3 = TreeNode(1)
    n1.add_child(n2)
    n1.add_child(n3)

    assert num_repeated_ancestors(n1) == 1

def test_task3_8()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(0)
    n1.add_child(n2)
    n1.add_child(n3)
    n2.add_child(n4)

    assert num_repeated_ancestors(n1) == 1

def test_task3_9()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(0)
    n5 = TreeNode(0)
    n1.add_child(n2)
    n1.add_child(n3)
    n2.add_child(n4)
    n3.add_child(n5)

    assert num_repeated_ancestors(n1) == 2

def test_task3_10()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(0)
    n5 = TreeNode(0)
    n6 = TreeNode(2)
    n1.add_child(n2)
    n1.add_child(n3)
    n2.add_child(n4)
    n3.add_child(n5)
    n3.add_child(n6)

    assert num_repeated_ancestors(n1) == 3

def test_task3_11()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(0)
    n5 = TreeNode(0)
    n6 = TreeNode(2)
    n7 = TreeNode(1)
    n1.add_child(n2)
    n1.add_child(n3)
    n2.add_child(n4)
    n3.add_child(n5)
    n3.add_child(n6)
    n4.add_child(n7)

    assert num_repeated_ancestors(n1) == 4

def test_task3_12()  -> None:
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(0)
    n5 = TreeNode(0)
    n6 = TreeNode(2)
    n7 = TreeNode(1)
    n8 = TreeNode(3)
    n9 = TreeNode(1)
    n1.add_child(n2)
    n1.add_child(n3)
    n2.add_child(n4)
    n3.add_child(n5)
    n3.add_child(n6)
    n4.add_child(n7)
    n4.add_child(n8)
    n6.add_child(n9)

    assert num_repeated_ancestors(n1) == 4

def test_task4_1()  -> None:
    c = Circle(1)
    assert c.area() - pi < 0.001
    assert c.perimeter() - 2*pi < 0.001
    assert c.is_symmetric()

def test_task4_2()  -> None:
    c = Circle(2)
    assert c.area() - 4*pi < 0.001
    assert c.perimeter() - 4*pi < 0.001
    assert c.is_symmetric()

def test_task4_3()  -> None:
    c = Circle(5.2)
    assert c.area() - 27.04*pi < 0.1
    assert c.perimeter() - 10.4*pi < 0.001
    assert c.is_symmetric()

def test_task4_4()  -> None:
    r = Rectangle(1, 2)
    assert r.area() == 2
    assert r.perimeter() == 6
    assert not r.is_symmetric()

def test_task4_5()  -> None:
    r = Rectangle(4, 3.6)
    assert r.area() - 14.4 < 0.001
    assert r.perimeter() - 15.2 < 0.001
    assert not r.is_symmetric()

def test_task4_6()  -> None:
    r = Rectangle(5, 5)
    assert r.area() == 25
    assert r.perimeter() == 20
    assert r.is_symmetric()

def test_task5_1()  -> None:
    s = Square(1)
    assert s.area() == 1
    assert s.perimeter() == 4
    assert s.is_symmetric()

def test_task5_2()  -> None:
    s = Square(2)
    assert s.area() == 4
    assert s.perimeter() == 8
    assert s.is_symmetric()

def test_task5_3()  -> None:
    s = Square(11.25)
    assert s.area() - 126.5625 < 0.001
    assert s.perimeter() - 45 < 0.001
    assert s.is_symmetric()
