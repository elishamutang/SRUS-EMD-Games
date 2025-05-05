class PlayerBNode:
    def __init__(self, player) -> None:
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player

    @property
    def key(self):
        return self.player.name

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, player) -> None:
        self._left = player

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, player) -> None:
        self._right = player

    def __str__(self):
        return f"(Key: {self.key}, Left: {self.left}, Right: {self.right})"