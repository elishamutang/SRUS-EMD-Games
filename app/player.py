import hashlib, math
import sys
from typing import Self
from app.player_node import PlayerNode


class Player:
    def __init__(self, player_id: str, name: str) -> None:
        self._id = player_id
        self._name = name

    @property
    def uid(self) -> str:
        """Get player ID."""
        return self._id

    @property
    def name(self) -> str:
        """Get player name."""
        return self._name

    def __str__(self) -> str:
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

        if isinstance(key, str):
            digest = hashlib.sha256(key.encode()).digest()
            return int.from_bytes(digest, "big") % sys.hash_info.modulus

        raise TypeError(f"Expected type string instead of {type(key)}")

    def __hash__(self) -> int:
        return self.custom_hash(self.uid)

    def __eq__(self, other: Self | PlayerNode) -> bool:
        if isinstance(other, PlayerNode):
            return self.uid == other.key

        return self.uid == other.uid