from typing import List


class TreeNode:
    value: int
    children: List["TreeNode"]

    def __init__(self, value: int):
        self.value = value
        self.children = []

    def add_child(self, child: "TreeNode") -> None:
        self.children.append(child)

    def is_leaf(self) -> bool:
        return len(self.children) == 0