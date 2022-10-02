from dsLinkedList import  DoubleLinkedList


class Queue:
    def __init__(self):
        self._list = DoubleLinkedList()

    def enqueue(self, value):
        self._list.add(value)

    def deque(self):
        val = self._list.front()
        self._list.remove_first()
        return val

    def front(self):
        return self._list.front()

    def is_empty(self):
        return self._list.size == 0

    def __len__(self):
        return self._list.size


# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(3)
# print(my_queue.front())
# my_queue.enqueue(35)
# my_queue.enqueue(300)
# my_queue.enqueue(33)
# print(my_queue.front())
# print(my_queue.front())
# print(len(my_queue))
# my_queue.deque()
# print(my_queue.front())
# print(len(my_queue))

