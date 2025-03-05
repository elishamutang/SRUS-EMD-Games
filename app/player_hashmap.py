from player_list import PlayerList
from player import Player

class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for i in range(0, self.SIZE)]

    def __getitem__(self, key: str) -> None:
        pass

    def __setitem__(self, key: str, name: str) -> None:
        pass

    def __len__(self):
        pass

    def __delitem__(self, key: str) -> None:
        pass


test = PlayerHashMap()
print(test.hashmap)