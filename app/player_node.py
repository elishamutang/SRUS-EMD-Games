class PlayerNode:

    def __init__(self, player):
        self._player = player
        self._next = None
        self._prev = None

    def __str__(self):
        return (f"Previous player: {self.prev.key if self.prev is not None else None},"
                f"\nCurrent player: {self.key},"
                f"\nNext player: {self.next.key if self.next is not None else None}")

    @property
    def key(self):
        """Return player ID"""
        return self._player.uid

    @property
    def next(self):
        """Get next Player"""
        return self._next

    @next.setter
    def next(self, player):
        """Set next player"""
        self._next = player

    @property
    def prev(self):
        """Get previous Player"""
        return self._prev

    @prev.setter
    def prev(self, player):
        """Set previous player"""
        self._prev = player