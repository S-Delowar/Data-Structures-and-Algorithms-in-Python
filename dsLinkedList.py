class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def _remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self._remove_node(node)
            node = node.next

    def front(self):
        return self.head.val

    def back(self):
        return self.tail.val

    def remove_first(self):
        if self.head is not  None:
            self._remove_node(self.head)

    def remove_last(self):
        if self.tail is not None:
            self._remove_node(self.tail)

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return  f"[{', '.join(str(val) for val in vals)}]"


# my_list = DoubleLinkedList()
# my_list.add(1)
# my_list.add(2)
# my_list.add(5)
# my_list.add(5)
# my_list.add(23)
# print(my_list)
# my_list.remove(2)
# print(my_list)
# my_list.remove(23)
# print(my_list)
# my_list.add(2)
# my_list.add(5)
# my_list.add(5)
# my_list.add(23)
# print(my_list)
# my_list.remove_last()
# print(my_list)
# print(my_list.size)
# my_list.remove_first()
# print(my_list)
# print(my_list.size)
