from typing import Optional, Any
from collections.abc import Iterable


class List:

    def __init__(self, values: Optional[Iterable] = None):
        if values is not None:
            self._list = list(values)
        else:
            self._list = []

    def __repr__(self):
        return f"<List {self._list}>"

    def add(self, data: Any):
        self._list.append(data)

    def insert_before(self, index: int, data: Any):
        self._list.insert(index, data)

    def get(self, index: int):
        return self._list[index]

    def set(self, index: int, data: Any):
        self._list[index] = data

    def index_of(self, data: Any):
        try:
            return self._list.index(data)
        except ValueError:
            return -1

    def remove(self, index: int):
        self._list = self._list[:index] + self._list[index+1:]

    def clear(self):
        self._list = []

    def reversed(self):
        return List(reversed(self._list))

    @property
    def size(self):
        return len(self._list)

    @property
    def iterator(self):
        return iter(self._list)

    # implementing the python container API using the methods above
    def __len__(self):
        return self.size

    def __getitem__(self, index: int):
        return self.get(index)

    def __setitem__(self, index: int, data: Any):
        self.set(index, data)

    def __delitem__(self, index: int):
        self.remove(index)

    def __iter__(self):
        return self.iterator

    def __reversed__(self):
        return self.reversed()

    def __contains__(self, data):
        return self.indexOf(data) != -1

    # TODO tesztek
