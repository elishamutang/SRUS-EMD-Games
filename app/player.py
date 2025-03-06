import hashlib, math
from typing import Self

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

    @classmethod
    def custom_hash(cls, key: str) -> int:
        """
        Hash function that uses the SHA256 hash function
        https://docs.python.org/3/library/hashlib.html
        https://en.wikipedia.org/wiki/SHA-2
        https://en.wikipedia.org/wiki/SHA-2#Pseudocode

        Parameters:
            key (str): Player uid.

        Returns:
            hash (int)
        """
        return int(hashlib.sha256(key.encode()).hexdigest(), 16) % 10

    def __hash__(self):
        return self.custom_hash(self.uid)

    def __eq__(self, other: Self) -> bool:
        return self.uid == other.uid


test = Player('123', 'John')
test2 = Player('123', 'Jane')

hash_val = hash(test)
print(hash_val)

custom_hash_val = Player.custom_hash(test.uid)
print(custom_hash_val)