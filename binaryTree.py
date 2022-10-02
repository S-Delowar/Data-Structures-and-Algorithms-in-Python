from queue import Queue
from binaryTreePrinter import BinaryTreePrinter
from stack import Stack


class TreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                checking_node = nodes.deque()
                if checking_node.left is None:
                    checking_node.left = TreeNode(val)
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val)
                    return
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)

    def contains(self, val):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            node = nodes.pop()
            print('Checking node: ', node.val)
            if node.val == val:
                return True
            if node.left is not None:
                nodes.push(node.left)
            if node.right is not None:
                nodes.push(node.right)
        return False

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)

my_tree = BinaryTree()

for c in [10,2,3,4,5,6,7,8,9, 20, 22]:
    my_tree.insert(c)
    print(my_tree)

print(my_tree.contains(5))