from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for i in range(0, self.SIZE)]

    def __getitem__(self, key: str | Player) -> PlayerNode:
        """
        Returns PlayerNode object of selected key.
        Args:
            key (str): Player ID.
            key (obj): Player object.

        Returns:
            PlayerNode (obj)
        """
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
        """
        Add new player to hashmap or update existing player.
        Args:
            key (str): Player ID.
            name (str): Player name.

        Returns:
            None
        """

        # Create new Player and PlayerNode object.
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
            try:
                # Find if player exists in hash map.
                player_clone = self[key]

                if player_clone.next is not None:
                    player_clone.next.prev = new_player_node
                    new_player_node.next = player_clone.next

                if player_clone.prev is not None:
                    player_clone.prev.next = new_player_node
                    new_player_node.prev = player_clone.prev

                # Replace list and add to hashmap.
                new_player_list = PlayerList()
                new_player_list.push(new_player_node)

                self.hashmap[player_list_index] = new_player_list
                # print(self[key].prev, self[key], self[key].next)
                # print(self.hashmap[player_list_index].display())

            except KeyError:
                # If key not found in hashmap, add to corresponding player_list.
                player_list.push(new_player_node)

        else:
            player_list.push(new_player_node)

    def __len__(self) -> int:
        """Returns number of players in hashmap."""
        length = 0

        for i in range(self.SIZE):
            length += len(self.hashmap[i])

        return length

    def __delitem__(self, key: str) -> None:
        """
        Deletes player from player list in player hashmap.
        Args:
            key (str): Player ID.

        Returns:
            None
        """
        try:

            if len(self) == 0:
                raise ValueError('Hashmap is empty.')

            # Get player node and corresponding player_list
            selected_player = self[key]
            player_list = self.hashmap[self.get_index(key)]

            # Pop player_list if list only contains one player.
            if len(player_list) == 1:
                player_list.pop()
            else:
                if selected_player.next is not None:
                    selected_player.next.prev = None
                    selected_player.next = None

                if selected_player.prev is not None:
                    selected_player.prev.next = None
                    selected_player.prev = None
        except KeyError:
            raise


    def display(self) -> None:
        """
        Print index of PlayerList and the players in the list if list has one or more player.

        Returns:
            None
        """

        for index, player_list in enumerate(self.hashmap):
            if len(player_list) >= 1:
                print(f"\nPlayer list index: {index}")
                print(f"Players are:")

                current = player_list.head
                print(current)
                while current.next is not None:
                    current = current.next
                    print(current)


# Tests
# test_hashmap = PlayerHashMap()
# test_hashmap['123'] = 'John'
# test_hashmap['456'] = 'Jane'
# test_hashmap['789'] = 'Jeremy'
# test_hashmap['123'] = 'Aaron'
# test_hashmap['888'] = 'Heng'
# test_hashmap['789'] = 'Remy'

# print(test_hashmap['888'])

# Get
# print(test_hashmap['123'])

# Delete
# del test_hashmap['456']
# del test_hashmap['123']
# del test_hashmap['789']
# del test_hashmap['888']
# del test_hashmap['123']
# del test_hashmap['111']

# Display
# test_hashmap.display()
#
# print("\n==========================================")
# print(f"Length of hashmap: {len(test_hashmap)}")
# print("==========================================")