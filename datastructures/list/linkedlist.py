from typing import Optional, Any
from list import List


class ListNode:

    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["ListNode"] = None

    def __repr__(self):
        return f"<ListNode: {self.data}>"


class LinkedList(List):

    def __init__(self, values = None):
        self.head: Optional[ListNode] = None

        if values is not None:
            for v in values:
                self.add(v)

    def __repr__(self):
        return f"<LinkedList: {self.head} ...>"

    # O(n)
    def add(self, data: Any):
        new_node = ListNode(data)

        # epmty
        if self.head is None:
            self.head = new_node

        else:
            tmp = self.head

            while tmp.next is not None:
                tmp = tmp.next

            tmp.next = new_node

    # O(n) (search) + O(1)
    def insert_before(self, index, data):
        new_node = ListNode(data)

        # empty
        if self.head is None:
            self.head = new_node

        # new head
        elif index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            node = self.head
            while index > 0 and node.next is not None:
                index -= 1
                node = node.next

            new_node.next = node.next
            node.next = new_node

    def _get(self, index):
        node = self.head

        while index > 0 and node is not None:
            index -= 1
            node = node.next

        return node

    # O(n)
    def get(self, index):
        return getattr(self._get(index), "data", None)

    # O(n)
    def set(self, index, data):
        node = self._get(index)
        if node:
            node.data = data
        else:
            raise KeyError("Index out of range.")

    # O(n)
    def index_of(self, data):
        node = self.head
        pos = 0
        while node is not None:
            if node.data == data:
                return pos
            pos += 1
            node = node.next

        return -1

    # O(n)
    def remove(self, index):
        # head
        if index == 0 and self.head is not None:
            self.head = self.head.next
        else:
            node = self.head
            while node is not None and index > 1:
                index -= 1
                node = node.next

            if node is not None:
                if node.next is not None:
                    node.next = node.next.next

    # O(1)
    def clear(self):
        self.head = None

    # O(n)
    def reversed(self):
        node = self.head
        rlist = LinkedList()
        while node is not None:
            newnode = ListNode(node.data)
            if rlist.head:
                newnode.next = rlist.head
                rlist.head = newnode
            else:
                rlist.head = newnode
            node = node.next

        return rlist

    # O(n)
    @property
    def size(self):
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.next

        return size

    # O(1) (next element)
    @property
    def iterator(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
