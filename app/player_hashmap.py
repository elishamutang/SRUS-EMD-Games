from player_list import PlayerList
from player import Player
from player_node import PlayerNode

class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for i in range(0, self.SIZE)]

    def __getitem__(self, key: str | Player) -> int:
        # Find index based on Player hash.
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
        player_list_index = hash(new_player) % self.SIZE

        # Access PlayerList at player_list_index and place new_player_node if it does not already exist.
        player_list = self.hashmap[player_list_index]

        if player_list.is_empty:
            player_list.push(new_player_node)
        else:
            # If new_player already exists, overwrite it
            current = player_list.head

            while current.value != key and current is not None:
                current = current.next

            current.value = key

    def __len__(self):
        pass

    def __delitem__(self, key: str) -> None:
        pass