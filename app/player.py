class Player:
    def __init__(self, player_id: str, name: str) -> None:
        self._id = player_id
        self._name = name

    @property
    def uid(self) -> str:
        """Return player ID."""
        return self._id

    @property
    def name(self) -> str:
        """Return player name."""
        return self._name

    def __str__(self) -> str:
        return f"(ID: {self.uid}, Name: {self.name})"