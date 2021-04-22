"""
    Lab Assignment 7
    11/23/20
    Assignment 7: Test BinaryTree class
"""
from node import Node
from binary_tree import BinaryTree


def test_binary_tree():
    """
    The function tests if the binary tree is working properly.
    """
    # build the binary tree
    root_node = Node(3)
    binary_tree = BinaryTree(root_node)
    binary_tree.insert(Node(2))
    binary_tree.insert(Node(5))
    binary_tree.insert(Node(1))

    # replace temporary with none
    binary_tree.insert(Node('Temporary'))

    binary_tree.insert(Node(4))
    binary_tree.insert(Node(6))

    # replace temporary with none
    binary_tree._left_child._right_child = None

    # right tree to the lowest node 6
    binary_tree._right_child._right_child._right_child = BinaryTree(Node(7))

    # traverse binary tree
    print('Traverse Preorder-----------------')
    binary_tree.traverse('preorder')
    print()

    print('Traverse Inorder-----------------')
    binary_tree.traverse('inorder')
    print()

    print('Traverse Postorder-----------------')
    binary_tree.traverse('postorder')
    print()

    # use explanation (not code) from https://www.geeksforgeeks.org/find-maximum-or-minimum-in-binary-tree/ to build
    # maximum method
    print(f'maximum node value: {binary_tree.maximum()}')

    # height function operates well only in this specific situations
    print(f'height of binary tree: {BinaryTree.height(binary_tree)} levels (includes level 0 -> levels 0-3)')

    print(f'size of binary tree: {BinaryTree.size(binary_tree)} nodes')

    print(f'if node with value 5 is found in binary tree: {binary_tree.search(5)}')


if __name__ == '__main__':
    test_binary_tree()

"""
Traverse Preorder-----------------
3
2
1
5
4
6
7

Traverse Inorder-----------------
1
2
3
4
5
6
7

Traverse Postorder-----------------
1
2
4
7
6
5
3

maximum node value: 7
height of binary tree: 3 levels (includes level 0 -> levels 0-3)
size of binary tree: 7 nodes
"""
