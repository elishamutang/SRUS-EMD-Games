class PlayerList:

    def __init__(self):
        self._head = None
        self._tail = None

    def __len__(self):
        length = 0
        current_node = self.head

        if current_node is None:
            return length
        else:
            while current_node is not None:
                current_node = current_node.next
                length += 1

            return length

    @property
    def is_empty(self):
        return len(self) == 0

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        self._head = head

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, tail):
        self._tail = tail

    # Insert new node at head of list.
    def shift(self, node):
        if self.is_empty:
            self.head = node
        else:
            current_node = self.head

            if current_node.next is None:
                self.tail = current_node

            while current_node.prev is not None:
                current_node = current_node.prev

            self.head = node
            node.next = current_node
            current_node.prev = self.head