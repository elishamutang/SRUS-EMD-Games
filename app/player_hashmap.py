from player_list import PlayerList
from player import Player

class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for i in range(0, self.SIZE)]

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, name):
        pass

    def __len__(self):
        pass

    def __delitem__(self, key):
        pass


test = PlayerHashMap()
print(test.hashmap)