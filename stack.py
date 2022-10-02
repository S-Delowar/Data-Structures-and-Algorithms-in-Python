from dsLinkedList import DoubleLinkedList


class Stack:
    def __init__(self):
        self._list = DoubleLinkedList()

    def push(self, val):
        self._list.add(val)

    def pop(self):
        val = self._list.back()
        self._list.remove_last()
        return val

    def is_empty(self):
        self._list.size == 0

    def peak(self):
        return self._list.back()

    def __len__(self):
        return self._list.size


my_stack = Stack()
my_stack.push(1)
my_stack.push(100)
my_stack.push(220)
my_stack.push(310)
my_stack.push(400)
print(my_stack.peak())
print(my_stack.pop())
print(my_stack.is_empty())
print(len(my_stack))