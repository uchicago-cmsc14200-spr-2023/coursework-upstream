"""
CMSC 14200, Spring 2023
Homework #2

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Tuple, Union, Optional
from trees import ExprNode, BSTNode, BSTEmpty


#### Task 1 ####

class Boolean(ExprNode):
    """
    Class to represent a boolean value (True or False)
    """


class And(ExprNode):
    """
    Class to represent the "and" operator
    """


class Or(ExprNode):
    """
    Class to represent the "or" operator
    """


class Not(ExprNode):
    """
    Class to represent the "not" operator
    """


#### Task 2 ####

def verify_avl(t: Union[BSTEmpty, BSTNode]) -> bool:
    """
    Determine whether or not a BST is an AVL tree

    Input:
        t (BST): the tree

    Returns (bool): True if t is an AVL tree, False otherwise
    """
    raise NotImplementedError


#### Task 3 ####

class BSTEmptyOpt:
    """
    Empty (Optimized) BST Tree
    """

    # No constructor needed (nothing to initialize)

    @property
    def is_empty(self) -> bool:
        """
        Returns: True if the tree is empty, False otherwise
        """
        return True

    @property
    def is_leaf(self) -> bool:
        """
        Returns: True if the tree is a leaf node, False otherwise
        """
        return False

    @property
    def num_nodes(self) -> int:
        """
        Returns: The number of nodes in the tree
        """
        return 0

    @property
    def height(self) -> int:
        """
        Returns: The height of the tree
        """
        return 0

    def contains(self, n: int) -> bool:  # pylint: disable=unused-argument
        """
        Determines whether a value is contained in the tree.

        Args:
            n: The value to check

        Returns: True if the value is contained in the tree,
            False otherwise.
        """
        return False

    def insert(self, n: int) -> "BSTNodeOpt":
        """
        Inserts a value into the tree

        Args:
            n: Value to insert

        Returns: A new tree with the value inserted into it
        """
        return BSTNodeOpt(n, BSTEmptyOpt(), BSTEmptyOpt())


class BSTNodeOpt:
    """
    (Optimized) BST Tree Node
    """

    value: int
    left: Union[BSTEmptyOpt, "BSTNodeOpt"]
    right: Union[BSTEmptyOpt, "BSTNodeOpt"]

    def __init__(self, n: int,
                 left: Union[BSTEmptyOpt, "BSTNodeOpt"],
                 right: Union[BSTEmptyOpt, "BSTNodeOpt"]):
        """
        Constructor

        Args:
            n: Value associated with the tree node
            left: Left child tree
            right: Right child tree
        """
        self.value = n
        self.left = left
        self.right = right

    @property
    def is_empty(self) -> bool:
        """
        Returns: True if the tree is empty, False otherwise
        """
        return False

    @property
    def is_leaf(self) -> bool:
        """
        Returns: True if the tree is a leaf node, False otherwise
        """
        return self.left.is_empty and self.right.is_empty

    @property
    def num_nodes(self) -> int:
        """
        Returns: The number of nodes in the tree
        """
        return 1 + self.left.num_nodes + self.right.num_nodes

    @property
    def height(self) -> int:
        """
        Returns: The height of the tree
        """
        return 1 + max(self.left.height, self.right.height)

    @property
    def balance_factor(self) -> int:
        """
        Returns: Balance factor of the tree
        """
        return self.right.height - self.left.height

    def contains(self, n: int) -> bool:
        """
        Determines whether a value is contained in the tree.

        Args:
            n: The value to check

        Returns: True if the value is contained in the tree,
            False otherwise.
        """
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n: int) -> "BSTNodeOpt":
        """
        Inserts a value into the tree

        Args:
            n: Value to insert

        Returns: A new tree with the value inserted into it
        """
        if n < self.value:
            return BSTNodeOpt(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return BSTNodeOpt(self.value, self.left, self.right.insert(n))
        else:
            return self


#### Task 4 ####

class Board:
    """
    Class to represent a game board.

    Attributes:
        rows (int): number of rows
        cols (int): number of columns
        board (list): the game board
        location_of_pieces (dictionary): the location of each piece on the board

    Methods:
        add_piece: add a piece represented by a string to the board
    """
    rows: int
    cols: int
    board: List[List[Optional[str]]]
    location_of_pieces: Dict[str, List[Tuple[int, int]]]

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.board = [[None] * cols for _ in range(rows)]
        self.location_of_pieces = {}

    def add_piece(self, piece: str, location: Tuple[int, int]) -> bool:
        """
        Add a piece represented by a string to the board.

        Inputs:
            piece (string): the piece to add
            location (tuple): the (row, column) location of where to add
                the piece

        Returns (bool): True if the piece was added successfully,
            False otherwise
        """
        row, col = location

        if self.board[row][col] is None:
            self.board[row][col] = piece
            if piece in self.location_of_pieces:
                self.location_of_pieces[piece].append(location)
            else:
                self.location_of_pieces[piece] = [location]
            return True
        return False

    # Add your is_full property here


#### Task 5 ####

def get_moves(b: Board, piece: str) -> List[Tuple[int, int]]:
    """
    Get all possible moves for a piece in a two player game of Reversi

    Input:
        b (Board): the board
        piece (string): the piece

    Return (list of tuples): A list of all possible moves for
        piece on the Reversi board b, according to the rules of Reversi
    """
    raise NotImplementedError
