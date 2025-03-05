class Player:
    def __init__(self, player_id: str, name: str) -> None:
        self._id = player_id
        self._name = name

    @property
    def uid(self):
        """Get player ID."""
        return self._id

    @property
    def name(self):
        """Get player name."""
        return self._name

    def __str__(self):
        return f"(ID: {self.uid}, Name: {self.name})"