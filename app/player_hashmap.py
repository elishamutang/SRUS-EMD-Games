from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for i in range(0, self.SIZE)]

    def __getitem__(self, key: str | Player) -> Player:
        player_list = self.hashmap[self.get_index(key)]

        if player_list.is_empty:
            raise KeyError('Key not found.')

        current = player_list.head

        while current.key != key and current.next is not None:
            current = current.next

        if current.key != key:
            raise KeyError('Key not found.')

        return current

    def get_index(self, key: str | Player) -> int:
        """
        Returns player index to determine which player list it belongs to.
        Args:
            key (str): Player ID.
            key (obj): Player object.

        Returns:
            index (int)
        """
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
        player_list_index = self.get_index(new_player)

        # Access PlayerList at player_list_index and place new_player_node if it does not already exist.
        player_list = self.hashmap[player_list_index]

        if player_list.is_empty is False:
            """
            If player_list is NOT empty, check if player with same key is already in the list. If it is:
                a) Update the name, if not
                b) add to player_list.
            """

            current = player_list.head
            prev_node = None

            while current.key != key and current.next is not None:
                prev_node = current
                current = current.next

            if current.key == key:

                if prev_node is not None:
                    prev_node.next = new_player_node

                current.next.prev = new_player_node

                new_player_node.prev = prev_node
                new_player_node.next = current.next

                current.next = None
                current.prev = None

                # Construct new PlayerList instance and overwrite existing list in player hashmap.
                new_player_list = PlayerList()
                new_player_list.push(new_player_node)

                self.hashmap[player_list_index] = new_player_list

            else:
                print(f"New player key {key} added to player list at index {player_list_index}")
                player_list.push(new_player_node)

        else:
            print(f"Key where list (index {player_list_index}) is empty: {key}")
            player_list.push(new_player_node)


    def __len__(self) -> int:
        length = 0

        for i in range(self.SIZE):
            length += len(self.hashmap[i])

        return length

    def __delitem__(self, key: str) -> None:
        print(f"Key {key} to be deleted.")

        # Get corresponding player_list
        player_list = self.hashmap[self.get_index(key)]



    def display(self):
        pass


# Tests
test_hashmap = PlayerHashMap()
test_hashmap['123'] = 'John'
test_hashmap['456'] = 'Jane'
test_hashmap['789'] = 'Jeremy'
test_hashmap['123'] = 'Aaron'
test_hashmap['888'] = 'Heng'

print(test_hashmap['888'])
# Delete
del test_hashmap['456']

print("\n==========================================")
print(f"Length of hashmap: {len(test_hashmap)}")
print("==========================================")