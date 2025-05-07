from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self) -> None:
        self._root = None

    @property
    def root(self) -> PlayerBNode:
        """Return root node of PlayerBST."""
        return self._root

    @root.setter
    def root(self, node: PlayerBNode):
        self._root = node

    def insert(self, player: Player) -> PlayerBNode:
        """
        Insert Player objects into PlayerBST.

        Args:
            player (Player): Player object.

        Returns:
            Player Node (PlayerBNode).
        """

        new_node = PlayerBNode(player)

        if self.root is None:
            self.root = new_node
            return self.root

        if new_node.key < self.root.key:

            left_subtree = PlayerBST()
            left_subtree.root = self.root.left

            new_left_subtree = left_subtree.insert(new_node.player)
            self.root.left = new_left_subtree

        elif new_node.key > self.root.key:

            right_subtree = PlayerBST()
            right_subtree.root = self.root.right

            new_right_subtree = right_subtree.insert(new_node.player)
            self.root.right = new_right_subtree

        else:
            # print(f"New node {new_node} is a duplicate of {self.root}")
            self.root = new_node

        return self.root

    def search(self, name: str) -> Player | None:
        """
        Search for player name and return player.

        Args:
            name (str): Player name.

        Returns:
            Player (Player).
        """

        print(f"Searching for {name}")

        if self.root is None:
            return None

        if self.root.key == name:
            return self.root.player

        if name < self.root.key:

            left_subtree = PlayerBST()
            left_subtree.root = self.root.left
            print(f"Going down left subtree: {left_subtree.root}")

            player = left_subtree.search(name)
            print(f"{player} found in left subtree of {self.root}")
            return player
        elif name > self.root.key:

            right_subtree = PlayerBST()
            right_subtree.root = self.root.right
            print(f"Going down right subtree: {right_subtree.root}")

            player = right_subtree.search(name)
            print(f"{player} found in right subtree of {self.root}")
            return player

    def balance(self) -> None:
        """
        Balances an unbalanced BST.

        Returns:
            None
        """

        # Create a sorted list based on the unbalanced BST.
        sorted_arr = self.__create_list(self.root, [])

        print(f"Sorted arr: {sorted_arr}")

        # Create new balanced BST recursively.
        self.root = PlayerBST.__balance(sorted_arr)

    def __create_list(self, root: PlayerBNode, players: list[Player]) -> list | None:
        """
        Creates a sorted list from the current BST. Also known as the in-order traversal
        which returns a sorted list.

        Args:
            root (PlayerBNode): Root node.
            players list[Player]: List of players.

        Returns:
            sorted_arr (list[Player]) or None.
        """

        sorted_arr = players

        if root is None:
            return None

        self.__create_list(root.left, players)
        players.append(root.player)
        self.__create_list(root.right, players)

        return sorted_arr

    @staticmethod
    def __balance(sorted_arr: list[Player]) -> 'PlayerBST' or None:
        """
        Utility function to performing the 'balancing' of the unbalanced BST.

        Args:
            sorted_arr (list[Player]): Sorted players array.

        Returns:
            Balanced BST (PlayerBST) or None.
        """

        if len(sorted_arr) == 0:
            return None

        # Pick middle element and make that the root of the new Balanced BST.
        mid_idx = len(sorted_arr) // 2

        # Split sorted_arr
        left = sorted_arr[:mid_idx]
        right = sorted_arr[mid_idx + 1:]

        mid_element = sorted_arr.pop(mid_idx)

        # Create new BST
        new_bst = PlayerBST()
        new_bst.root = PlayerBNode(mid_element)

        new_bst.root.left = new_bst.__balance(left)
        new_bst.root.right = new_bst.__balance(right)

        return new_bst

    def __str__(self) -> str:
        return f"{self.root}"

    def __repr__(self) -> str:
        return f"PlayerBST[{self.root}]"

