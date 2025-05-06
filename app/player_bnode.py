from app.player import Player

class PlayerBNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def key(self) -> str:
        return self.player.name

    @property
    def left(self) -> 'PlayerBNode':
        return self._left

    @left.setter
    def left(self, player: 'PlayerBNode') -> None:
        self._left = player

    @property
    def right(self) -> 'PlayerBNode':
        return self._right

    @right.setter
    def right(self, player: 'PlayerBNode') -> None:
        self._right = player

    def __str__(self):
        return f"(Key: {self.key}, Left: {self.left}, Right: {self.right})"