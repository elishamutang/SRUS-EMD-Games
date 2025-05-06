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
            PlayerBNode
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
            Player.
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

    def __str__(self):
        return f"{self.root}"


# test = PlayerBST()
# player_one = Player('1', 'John', 10)
# player_two = Player('2', 'Jack' ,2)
# player_three = Player('3', 'Koala', 3)
# player_four = Player('5', 'Jake', 5)
# # player_five = Player('6', 'Lauren', 20)
# # player_six = Player('7', 'Lauren', 10)
# #
# #
# #
# test.insert(player_one)
# test.insert(player_two)
# test.insert(player_three)
# test.insert(player_four)
# # test.insert(player_five)
# # test.insert(player_six)
# # print(test.root.right.right.player)
#
# print(test)
# print(test.search('Chicken'))


