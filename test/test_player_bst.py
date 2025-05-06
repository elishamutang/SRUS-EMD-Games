import unittest
from app.player_bst import PlayerBST
from app.player_bnode import PlayerBNode
from app.player import Player

class TestPlayerBST(unittest.TestCase):

    def setUp(self):
        self.playerBST = PlayerBST()

    def test_insert_method_one_player_only(self):
        player_one = Player('1', 'John', 5)
        player_one_node = PlayerBNode(player_one)

        self.playerBST.insert(player_one)
        self.assertEqual(self.playerBST.root.player, player_one_node.player)

    def test_insert_smaller_key_at_left_node(self):
        player_one = Player('1', 'John', 5)
        player_two = Player('2', 'Jack', 10)

        player_two_node = PlayerBNode(player_two)

        self.playerBST.insert(player_one)
        self.playerBST.insert(player_two)

        self.assertEqual(self.playerBST.root.left.player, player_two_node.player)

    def test_insert_larger_key_at_right_node(self):
        player_one = Player('1', 'John', 5)
        player_two = Player('2', 'Koala', 6)

        player_two_node = PlayerBNode(player_two)

        self.playerBST.insert(player_one)
        self.playerBST.insert(player_two)

        self.assertEqual(self.playerBST.root.right.player, player_two_node.player)

    def test_insert_duplicate_key(self):
        player_one = Player('1', 'John', 0)
        player_two = Player('2', 'Jack', 2)
        player_three = Player('3', 'Koala', 3)
        player_four = Player('4', 'Jack', 10)

        self.playerBST.insert(player_one)
        self.playerBST.insert(player_two)
        self.playerBST.insert(player_three)
        self.playerBST.insert(player_four)

        duplicate_node = PlayerBNode(player_four)

        self.assertEqual(self.playerBST.root.left.player, duplicate_node.player)

    def test_search_BST_with_only_one_node(self):
        player_one = Player('1', 'John', 20)

        self.playerBST.insert(player_one)
        player_found = self.playerBST.search('John')

        self.assertEqual(player_found, player_one)

    def test_search_BST_with_value_that_does_not_exist_in_tree(self):
        player_one = Player('1', 'John', 0)
        player_two = Player('2', 'Jack', 2)
        player_three = Player('3', 'Koala', 3)

        self.playerBST.insert(player_one)
        self.playerBST.insert(player_two)
        self.playerBST.insert(player_three)

        player_found = self.playerBST.search('Chicken')

        self.assertIsNone(player_found)

    def test_search_BST_with_smaller_value_than_root_node(self):
        player_one = Player('1', 'John', 0)
        player_two = Player('2', 'Jack', 2)
        player_three = Player('3', 'Koala', 3)

        self.playerBST.insert(player_one)
        self.playerBST.insert(player_two)
        self.playerBST.insert(player_three)

        player_found = self.playerBST.search('Jack')
        self.assertEqual(player_found, player_two)

    def test_search_BST_with_greater_value_than_root_node(self):
        player_one = Player('1', 'John', 0)
        player_two = Player('2', 'Jack', 2)
        player_three = Player('3', 'Koala', 3)

        self.playerBST.insert(player_one)
        self.playerBST.insert(player_two)
        self.playerBST.insert(player_three)

        player_found = self.playerBST.search('Koala')
        self.assertEqual(player_found, player_three)