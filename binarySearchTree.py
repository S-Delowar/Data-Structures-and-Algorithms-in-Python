from binaryTree import  TreeNode
from binaryTreePrinter import  BinaryTreePrinter
from stack import Stack


class BST:
    def __init__(self):
        self.root = None

    def _insert_value(self, node, val):
        if node is None:
            return

        if node.val == val :
            return
        elif val < node.val :
            if node.left is None:
                node.left = TreeNode(val)
                return
            self._insert_value(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
                return
            self._insert_value(node.right, val)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_value(self.root, val)

    def _in_order(self, node):
        if node is None:
            return
        self._in_order(node.left)
        print(node.val, end=" ")
        self._in_order(node.right)

    def in_order(self):
        self._in_order(self.root)

    def contains(self, val):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            node = nodes.pop()
            print('Checking node: ', node.val)
            if node.val == val:
                return True
            elif val < node.val:
                if node.left is not None:
                    nodes.push(node.left)
            else:
                if node.right is not None:
                    nodes.push(node.right)
        return False

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


bst = BST()

# for x in [10,2,3,4,5,6,7,8,9, 20, 22]:
#     bst.insert(x)
#     print(bst)
# print(bst.in_order())
# print(bst.contains(5))