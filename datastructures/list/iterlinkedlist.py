from typing import Optional, Any
from list import List


class ListNode:

    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["ListNode"] = None

    def __repr__(self):
        return f"<ListNode: {self.data}>"


class IterLinkedList(List):

    def __init__(self, values = None):
        self.head: Optional[ListNode] = None

        if values is not None:
            for v in values:
                self.add(v)

    def __repr__(self):
        return f"<IterLinkedList: {self.head} ...>"

    # O(n)
    def add(self, data: Any):
        new_node = ListNode(data)

        # epmty
        if self.head is None:
            self.head = new_node
        else:
            for node in self.node_iterator: pass
            node.next = new_node

    # O(n) + O(1)
    def insert_before(self, index, data):
        new_node = ListNode(data)

        # empty
        if self.head is None:
            print("empty")
            self.head = new_node

        # new head
        elif index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            prev = self.head
            for idx, current in enumerate(self.node_iterator):
                if idx == index:
                    prev.next = new_node
                    new_node.next = current
                    break
                prev = current
            else:
                prev.next = new_node

    def _get(self, index):
        for idx, node in enumerate(self):
            if idx == index:
                return node

        return None

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
        for i, el in enumerate(self):
            if el == data:
                return i
        return -1

    # O(n)
    def remove(self, index):
        # head
        if index == 0 and self.head is not None:
            self.head = self.head.next
        else:
            prev = self.head
            for idx, node in enumerate(self.node_iterator):
                if idx == index:
                    prev.next = node.next
                    break

    # O(1)
    def clear(self):
        self.head = None

    # O(n)
    def reversed(self):
        node = self.head
        rlist = IterLinkedList()
        for node in self.node_iterator:
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
        for idx, node in enumerate(self.node_iterator): pass
        return idx

    @property
    def iterator(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    @property
    def node_iterator(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
