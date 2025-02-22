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

    # Insert item at the tail of list.
    def push(self, node):
        if self.is_empty:
            self.head = node
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            self.tail = node
            node.prev = current_node
            current_node.next = self.tail

    # Delete item from head of list.
    def unshift(self):
        if self.is_empty:
            return 'The list is empty.'

        current_node = self.head

        if current_node.next is not None:
            new_head = current_node.next
            new_head.prev = None
            current_node.next = None

            self.head = new_head
        else:
            self.head = None

    # Delete item from tail of list.
    def pop(self):
        if self.is_empty:
            return 'The list is empty.'

        current_node = self.tail

        if current_node.prev is not None:
            new_tail = current_node.prev
            new_tail.next = None
            current_node.prev = None

            # QUESTION: If list has 2 elements and we invoke pop() on it, does head == tail ?
            self.tail = new_tail
        else:
            self.tail = None
            self.head = self.tail
