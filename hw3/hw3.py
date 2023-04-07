"""
CMSC 14200, Spring 2023
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
from typing import List, Set, Dict, Tuple

from graph import Vertex, Graph


#### Task 1 ####

def num_indegree_gt_outdegree(graph: Graph) -> int:
    """
    Count how many vertices have in-degree > out-degree

    Input:
        graph (Graph): the graph

    Returns (int): the count
    """
    raise NotImplementedError


#### Task 2 ####

def reachable_in(graph: Graph, vertex: str, hops: int) -> Set[str]:
    """
    Determine the set of vertices in a graph reachable from a starting point in
    at most "hops" steps

    Inputs:
        graph (Graph): the graph
        vertex (str): the name of the starting vertex
        hops (int): the maximum number of steps away from the starting point

    Returns (Set[str]): the names of vertices reachable under the constraint
    """
    raise NotImplementedError


#### Task 3 ####

def flood_fill(grid: List[List[bool]], start: Tuple[int, int]) -> None:
    """
    "Flood fill" (the paint-bucket tool) a grid of booleans
    Change a cell in the grid to black (True) and its neighboring cell, and
    their neighbors, stopping when encountering an already-black (True) cell in
    a given direction
    Directions are N, E, S, and W, but not diagonal

    Inputs:
        grid (List[List[bool]]): two-dimensional grid of boolean cells
        start (Tuple[int, int]): the coordinates of the starting cell
            Returns: nothing
        """
    raise NotImplementedError
