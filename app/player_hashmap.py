from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for i in range(0, self.SIZE)]

    def __getitem__(self, key: str | Player) -> int:
        # Return player index based on Player hash.
        if isinstance(key, Player):
            player_index = hash(key) % self.SIZE
        else:
            player_index = Player.custom_hash(key) % self.SIZE

        return player_index

    def __setitem__(self, key: str, name: str) -> None:
        # Create new player.
        new_player = Player(key, name)
        new_player_node = PlayerNode(new_player)

        # Find index of PlayerList where new player will be placed.
        player_list_index = self[new_player] # NOT SURE IF THIS IS GOOD PRACTICE OR NOT.

        # Access PlayerList at player_list_index and place new_player_node if it does not already exist.
        player_list = self.hashmap[player_list_index]

        # Check if player already exists.

        # And push to player list.
        player_list.push(new_player_node)

    def __len__(self):
        length = 0

        for i in range(self.SIZE):
            # print(len(self.hashmap[i]))
            length += len(self.hashmap[i])

        return length

    def __delitem__(self, key: str) -> None:
        pass


test_hashmap = PlayerHashMap()
test_hashmap['123'] = 'John'
test_hashmap['456'] = 'Jane'

print(len(test_hashmap))
for hashmap in test_hashmap.hashmap:
    if len(hashmap) >= 1:
        print(hashmap.display())