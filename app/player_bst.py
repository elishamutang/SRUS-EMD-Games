from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self) -> None:
        self._root = None

    @property
    def root(self):
        """Return root node of PlayerBST."""
        return self._root

    @root.setter
    def root(self, node):
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

            if self.root.left is not None:
                left_subtree = PlayerBST()
                left_subtree.root = self.root.left

                new_left_subtree = left_subtree.insert(new_node.player)
                self.root.left = new_left_subtree

                # print(f"Left subtree: {left_subtree}")
            else:
                self.root.left = new_node

        elif new_node.key > self.root.key:

            if self.root.right is not None:
                right_subtree = PlayerBST()
                right_subtree.root = self.root.right

                new_right_subtree = right_subtree.insert(new_node.player)
                self.root.right = new_right_subtree

                # print(f"Right subtree: {right_subtree}")
            else:
                self.root.right = new_node

        return self.root


    def search(self, name: str) -> str:
        """
        Search for player name and returns it.

        Args:
            name (str): Player name.

        Returns:
            Player name (str).
        """
        pass

    def __str__(self):
        return f"{self.root}"




test = PlayerBST()
player_one = Player('1', 'John', 10)
player_two = Player('2', 'Jack' ,2)
player_three = Player('3', 'Koala', 3)
player_four = Player('4', 'Bruh', 4)
player_five = Player('5', 'Jake', 5)
player_six = Player('6', 'Narnia', 20)

test.insert(player_one)
test.insert(player_two)
test.insert(player_three)
test.insert(player_four)
test.insert(player_five)
test.insert(player_six)
print(test)


