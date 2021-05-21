"""
Ask: If it's a binary search tree or just binary tree
Ask: If it's balanced or unbalanced

    Balanced trees are: red-black trees and AVL trees

A complete binary tree is a binary tree in which every level 
of the tree is fullu filled, except perhaps the last level.

A full binary tree is a tree in which every node has either zero or two children.
That is no node has zero children.

A perfect binary tree is one that is both full and complete. All leaf nodes'll 
be at the same level, and this level has the maximum number of nodes.
They have 2^k - 1 nodes (where k is the number of levels).
"""

class Node:
    val: str
    left: 'Node' = None
    right: 'Node' = None

class Tree:
    root: Node

    def inorder_traversal(self, n: Tree) -> None:
        """
        In-order traversal means to visit the left branch, 
        then the current node, and finally, the right branch.
        """
        if n:
            self.inorder_traversal(n.left)
            print(n.val)
            self.inorder_traversal(n.right)
    
    def preorder_traversal(self, n: Tree) -> None:
        """
        Pre-order traversal visits the current node before its children
        """
        if n:
            print(n.val)
            self.preorder_traversal(n.left)
            self.preorder_traversal(n.right)

    def postorder_traversal(self, n: Tree) -> None:
        """
        Post-order traversal visits the current node after its children
        """
        if n:
            self.postorder_traversal(n.left)
            self.postorder_traversal(n.right)
            print(n.val)
