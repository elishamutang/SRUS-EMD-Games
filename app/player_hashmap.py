from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]


    def __getitem__(self, key: str | Player) -> PlayerNode:
        """
        Returns PlayerNode object of selected key.
        Args:
            key (str): Player ID.
            key (Player): Player object.

        Returns:
            PlayerNode

        Raises:
            KeyError: If player does not exist in hashmap.
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
            key (Player): Player object.

        Returns:
            Index (int)
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

        Raises:
            KeyError: If player not found in player_list.
        """

        # Create new Player and PlayerNode object.
        new_player = Player(key, name)
        new_player_node = PlayerNode(new_player)

        # Find index of PlayerList where new player will be placed.
        player_list_index = self.get_index(new_player)

        # Access PlayerList at player_list_index and place new_player_node if it does not already exist.
        player_list = self.hashmap[player_list_index]

        # If player_list is empty OR no player found, push new player in list else update existing player name.
        if player_list.is_empty:
            player_list.push(new_player_node)
        else:
            try:
                # Find if player exists in hash map.
                player_clone = self[key]

                if player_clone == player_list.head:
                    player_list.unshift()
                    player_list.shift(new_player_node)
                elif player_clone == player_list.tail:
                    player_list.pop()
                    player_list.push(new_player_node)
                else:
                    new_player_node.next = player_clone.next
                    new_player_node.prev = player_clone.prev

                    new_player_node.next.prev = new_player_node
                    new_player_node.prev.next = new_player_node

                    player_clone.next = None
                    player_clone.prev = None

            except KeyError:
                # If key not found in hashmap, add to corresponding player_list.
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

        Raises:
            ValueError: If deleting from an empty hashmap.
            KeyError: If player does not exist in hashmap.
        """
        try:
            if len(self) == 0:
                raise ValueError('Hashmap is empty.')

            # Get corresponding player_list
            player_list = self.hashmap[self.get_index(key)]
            player_list.delete(key)
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
