"""
CMSC 14200, Spring 2023
Homework #1

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from typing import List, Tuple, Dict, Union, Optional
from abc import ABC, abstractmethod
from math import pi

from tree import TreeNode


def words_that_start_with(list_of_words, char_to_match):
    """
    Count the number of words in a list whose first character matches
    the given character to match.

    Inputs:
        list_of_words (list): the list of words
        char_to_match (string): the character to match

    Returns (int): the number of words that start with char_to_match
    """
    raise NotImplementedError("todo: words_that_start_with")


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

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[None] * cols for _ in range(rows)]
        self.location_of_pieces = {}

    def add_piece(self, piece, location):
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


def num_repeated_ancestors(t: TreeNode) -> int:
    """
    Find the number of nodes in a tree that have the
        same value as one of their ancestors.

    Inputs:
        t (TreeNode): the tree

    Returns (int): the number of nodes
    """
    raise NotImplementedError("todo: num_repeated_ancestors")


class Shape(ABC):
    """
    Class to represent a shape.

    Methods:
        area: compute the area of the shape
        perimeter: compute the perimeter of the shape
        is_symmetric: determines whether or not the shape is symmetric
            with respect to 90 degree clockwise rotation
    """

    @abstractmethod
    def area(self) -> float:
        """
        Computes the area of the shape

        Returns (float): Area of the shape
        """
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float:
        """
        Computes the perimeter of the shape

        Returns (float): Perimeter of the shape
        """
        raise NotImplementedError

    @abstractmethod
    def is_symmetric(self) -> bool:
        """
        Checks whether the shape is symmetric

        Returns (bool): True if the shape is symmetric,
            False otherwise.
        """
        raise NotImplementedError


class Circle(Shape):
    """
    Class to represent a circle.
    """


class Rectangle(Shape):
    """
    Class to represent a rectangle.
    """


class Square(Rectangle):
    """
    Class to represent a square.
    """
