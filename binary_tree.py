from node import Node
from collections import deque as deque


class BinaryTree:
    """
    This class creates a binary tree with a parent root node and two children binary trees.

    Attributes:
        root (Node) : root of binary tree
        left child (BinaryTree) : left child tree
        right child (BinaryTree) : right child tree
    """

    def __init__(self, root=None):
        """
        The constructor for the BinaryTree class.

        Parameter:
            root (Node) : root of the binary tree
        """
        self._root = root
        self._left_child = None
        self._right_child = None

    def insert(self, new_node):
        """
        This function inserts a new node into the binary tree.

        Parameters:
            new_node (Node) : new node
        """
        current_trees = deque()
        root_tree = self
        current_trees.appendleft(root_tree)

        while len(current_trees) > 0:
            new_tree = current_trees.popleft()
            if new_tree.left_child is None:
                new_tree.left_child = BinaryTree(new_node)
                break
            else:
                current_trees.append(new_tree.left_child)

            if new_tree.right_child is None:
                new_tree.right_child = BinaryTree(new_node)
                break
            else:
                current_trees.append(new_tree.right_child)

    def delete(self, node):
        """
        This function deletes the specified node in the binary tree.

        Parameters:
            node (Node) : node to be deleted
        """
        current_trees = deque()
        current_tree = self

        if BinaryTree.height(current_tree) == 1:
            current_tree.root = None
            return

        child_to_delete = None
        tree_to_delete_parent = None
        tree_to_delete = None
        tree_to_delete_data = None

        current_trees.appendleft(current_tree)

        while len(current_trees) > 0:
            current_tree = current_trees.popleft()
            try:
                if current_tree.left_child.root.data == node:
                    child_to_delete = 'left'
                    tree_to_delete_parent = current_tree
                    tree_to_delete = current_tree.left_child
                    tree_to_delete_data = tree_to_delete.root.data

                if current_tree.right_child.root.data == node:
                    child_to_delete = 'right'
                    tree_to_delete_parent = current_tree
                    tree_to_delete = current_tree.right_child
                    tree_to_delete_data = tree_to_delete.root.data

                if current_tree.left_child is not None:
                    current_trees.append(current_tree.left_child)

                if current_tree.right_child is not None:
                    current_trees.append(current_tree.right_child)
            except AttributeError:
                continue

        lowest_tree = self.lowest_node(self)

        if tree_to_delete == lowest_tree:
            if child_to_delete == 'left':
                tree_to_delete_parent.left_child = None
                return
            elif child_to_delete == 'right':
                tree_to_delete_parent.right_child = None
                return
            else:
                raise ValueError('Node is not left or right child')
        else:
            tree_to_delete.root.data = lowest_tree.root.data
            lowest_tree.root.data = tree_to_delete_data
            self.delete(lowest_tree.root.data)

    def search(self, value):
        """
        This function searches for a node with the specified value in binary tree.

        Parameters:
            value : value to find

        Return:
            true (Boolean) : result if node is found
            false (Boolean) : result if node is not found
        """
        if self:
            if self.root.data == value:
                return True

            node_left_tree = None
            if self.left_child:
                node_left_tree = self.left_child.search(value)

            if node_left_tree:
                return True

            if not node_left_tree:
                if self.right_child:
                    node_right_tree = self.right_child.search(value)
                    return node_right_tree

        return False

    def traverse(self, method):
        """
        This function traverses the binary tree in a specified order.

        Parameters:
            method : type of method use to transverse the tree (preorder, inorder, or postorder )
        """
        if self is None:
            return

        if method.lower() == 'preorder':
            print(self.root.data)
            if self is not None:
                if self.left_child is not None:
                    self.left_child.traverse(method)
                if self.right_child is not None:
                    self.right_child.traverse(method)

        if method.lower() == 'inorder':
            if self is not None:
                if self.left_child is not None:
                    self.left_child.traverse(method)
                print(self.root.data)
                if self.right_child is not None:
                    self.right_child.traverse(method)

        if method.lower() == 'postorder':
            if self is not None:
                if self.left_child is not None:
                    self.left_child.traverse(method)
                if self.right_child is not None:
                    self.right_child.traverse(method)
            print(self.root.data)

    # use explanation (not code) from https://www.geeksforgeeks.org/find-maximum-or-minimum-in-binary-tree/ to build
    # maximum method
    def maximum(self):
        """
        This function finds the the maximum value in the binary tree.

        Return:
            maximum value in the binary tree
        """
        if (self.left_child is None) and (self.right_child is None):
            return self.root.data
        if (self.left_child is not None) and (self.right_child is None):
            return max(self.root.data, self.left_child.root.data)
        if (self.left_child is None) and (self.right_child is not None):
            return max(self.root.data, self.right_child.root.data)

        if (self.left_child is not None) and (self.right_child is not None):
            return max([self.root.data, self.left_child.maximum(), self.right_child.maximum()])

    @staticmethod
    def size(tree, size_of_tree=0):
        """
        The function that calculates the size of the binary tree (total number of nodes in tree).

        Parameters:
            tree (BinaryTree): tree to calculate size for
            size of tree (int) : current size of the tree

        Return:
            size of tree (int) : current size of the tree
        """
        current_trees = deque()
        current_tree = tree
        current_trees.appendleft(current_tree)

        while len(current_trees) > 0:
            current_tree = current_trees.popleft()

            if current_tree is not None:
                size_of_tree += 1

            try:
                if current_tree.left_child is not None:
                    current_trees.append(current_tree.left_child)

                if current_tree.right_child is not None:
                    current_trees.append(current_tree.right_child)
            except AttributeError:
                continue

        return size_of_tree

    @staticmethod
    def height(tree):
        """
        This function calculates the height of the tree.

        Return:
            current_height: current height of the tree
        """
        if tree is None:
            raise ValueError('Tree is empty')
        left_height = 0
        left_tree = tree
        while left_tree is not None:
            left_tree = left_tree.left_child
            left_height += 1

        right_tree = tree
        right_height = 0
        while right_tree is not None:
            right_tree = right_tree.right_child
            right_height += 1

        current_height = max(left_height, right_height)
        return current_height - 1

    @staticmethod
    def lowest_node(tree):
        """
        This function serves as a helper function in determining the lowest node in the tree.

        Parameters:
            tree : tree that the lowest node is being found in

        Return:
            current tree : lowest tree with lowest node
        """
        current_trees = deque()
        current_tree = tree
        current_trees.appendleft(current_tree)

        while len(current_trees) > 0:
            current_tree = current_trees.popleft()
            if current_tree.left_child is not None:
                current_trees.append(current_tree.left_child)
            if current_tree.right_child is not None:
                current_trees.append(current_tree.right_child)

        return current_tree

    @property
    def root(self):
        """
        This function returns the root of the binary tree.

        Return:
            root (Node) : root of the tree
        """
        return self._root

    @root.setter
    def root(self, new_root):
        """
        This function changes the root of the binary tree.

        Parameter:
            new_root (Node) : new root for the tree
        """
        self._root = new_root

    @property
    def left_child(self):
        """
        This function returns the left child tree.

        Return:
            left child (BinaryTree) : left child tree
        """
        return self._left_child

    @property
    def right_child(self):
        """
        This function returns the right child tree.

        Return:
            right child (BinaryTree) : right child tree
        """
        return self._right_child

    @left_child.setter
    def left_child(self, new_left_child):
        """
        This function changes the left child tree.

        Return:
            left child (BinaryTree) : left child tree
        """
        self._left_child = new_left_child

    @right_child.setter
    def right_child(self, new_right_child):
        """
        This function changes the right child tree.

        Return:
            right child (BinaryTree) : right child tree
        """
        self._right_child = new_right_child
