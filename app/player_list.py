class PlayerList:
    """
    This is a double linked list implementation which represents the
    player list at Softwares-R-Us.

    Attributes:
        _head (obj): Pointer to first node in list.
        _tail (obj): Pointer to last node in list.
    """

    def __init__(self):
        self._head = None
        self._tail = None

    def __len__(self) -> int:
        """ Returns length of PlayerList class. """
        length = 0
        current_node = self.head

        while current_node is not None:
            current_node = current_node.next
            length += 1

        return length

    @property
    def is_empty(self) -> bool:
        """ Determines if list is emtpy. """
        return len(self) == 0

    @property
    def head(self):
        """ Returns head. """
        return self._head

    @property
    def tail(self):
        """ Returns tail. """
        return self._tail

    def shift(self, node) -> None:
        """
        Inserts new player (node) at the head of list.

        Args:
            node (obj): Player node.

        Returns:
            None.
        """
        if self.is_empty:
            self._head = node
        else:
            current_node = self.head

            if current_node.next is None:
                self._tail = current_node

            while current_node.prev is not None:
                current_node = current_node.prev

            self._head = node
            node.next = current_node
            current_node.prev = self.head

    def push(self, node) -> None:
        """
        Inserts new player (node) at the tail of list.

        Args:
            node (obj): Player node.

        Returns:
            None.
        """
        if self.is_empty:
            self._head = node
        else:
            current_node = self.tail

            if current_node is None:
                current_node = self.head

            self._tail = node
            node.prev = current_node
            current_node.next = self.tail

    def unshift(self) -> None:
        """
        Deletes first player from the list.

        Returns:
            None

        Raises:
            IndexError: If deleting from empty list.
        """
        if self.is_empty:
            raise IndexError('The list is empty.')

        current_node = self.head

        if current_node.next is not None:
            new_head = current_node.next
            new_head.prev = None
            current_node.next = None

            self._head = new_head
        else:
            self._head = None

    def pop(self) -> None:
        """
        Deletes last player (tail) from the list.

        Returns:
            None

        Raises:
            IndexError: If deleting from empty list.
        """
        if self.is_empty:
            raise IndexError('The list is empty.')

        current_node = self.tail

        if current_node is None:
            current_node = self.head

        if current_node.prev is not None:
            new_tail = current_node.prev
            new_tail.next = None
            current_node.prev = None

            self._tail = new_tail
        else:
            self._tail = None
            self._head = self.tail

    def delete(self, key: str) -> None:
        """
        Deletes player based on player key.
        Args:
            key (str): Player key.

        Returns:
            None

        Raises:
            IndexError: If deleting from empty list.
            ValueError: Player does not exist in list.
        """

        if self.is_empty:
            raise IndexError('The list is empty')

        if key == self.head.key:
            self.unshift()
        elif key == self.tail.key:
            self.pop()
        else:
            current_node = self.head

            while current_node.key != key:
                current_node = current_node.next

                if current_node is None:
                    raise ValueError('Player not found.')

            new_node = current_node.next
            new_node.prev = current_node.prev

            current_node.prev.next = new_node

            current_node.next = None
            current_node.prev = None

    # Show entire list and present in a readable manner.
    def display(self, forward: bool = True) -> None:
        """
        Prints out the entire player list in a readable manner.

        Args:
            forward (bool): True - displays list from head to tail.
                            False - displays list from tail to head.

        Return:
            None.
        """
        if self.is_empty:
            raise IndexError('The list is empty.')

        print('\nDouble linked list: \n')
        current_node = self.head

        if forward is False:
            current_node = self.tail
            while current_node is not None:
                if current_node == self.tail:
                    print(f'Tail\n {current_node}\n ||')
                elif current_node == self.head:
                    print(f'{current_node}\nHead')
                else:
                    print(f' {current_node}\n ||')

                current_node = current_node.prev
        else:
            while current_node is not None:
                if current_node == self.head:
                    print(f'Head\n {current_node}\n ||')
                elif current_node == self.tail:
                    print(f'{current_node}\nTail')
                else:
                    print(f' {current_node}\n ||')

                current_node = current_node.next
