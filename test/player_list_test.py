import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

class TestPlayerList(unittest.TestCase):

    def setUp(self):
        self.player_list = PlayerList()

    def test_add_to_head_on_empty_list(self):
        test_player_one = Player(123, 'Joe')
        test_player_one_node = PlayerNode(test_player_one)

        self.player_list.shift(test_player_one_node)

        self.assertEqual(self.player_list.is_empty, False)
        self.assertEqual(self.player_list.head.key, test_player_one_node.key)

    def test_add_to_head_on_non_empty_list(self):
        test_player_one = Player(123, 'Joe')
        test_player_one_node = PlayerNode(test_player_one)

        self.player_list.shift(test_player_one_node)

        test_player_two = Player(456, 'Smith')
        test_player_two_node = PlayerNode(test_player_two)

        self.player_list.shift(test_player_two_node)

        self.assertEqual(len(self.player_list), 2)
        self.assertEqual(self.player_list.head.key, 456)
        self.assertEqual(self.player_list.tail.key, 123)

    def test_add_to_tail_on_empty_list(self):
        test_player_one = Player(123, 'Joe')
        test_player_one_node = PlayerNode(test_player_one)

        self.player_list.push(test_player_one_node)

        self.assertEqual(self.player_list.is_empty, False)
        self.assertEqual(self.player_list.head.key, 123)

    def test_add_to_tail_on_non_empty_list(self):
        test_player_one = Player(123, 'Joe')
        test_player_one_node = PlayerNode(test_player_one)

        self.player_list.push(test_player_one_node)

        test_player_two = Player(456, 'Smith')
        test_player_two_node = PlayerNode(test_player_two)

        self.player_list.push(test_player_two_node)

        self.assertEqual(len(self.player_list), 2)
        self.assertEqual(self.player_list.tail.key, 456)

    def test_remove_item_from_head(self):
        test_player_one = Player(123, 'Joe')
        test_player_one_node = PlayerNode(test_player_one)

        test_player_two = Player(456, 'Smith')
        test_player_two_node = PlayerNode(test_player_two)

        self.player_list.push(test_player_one_node)
        self.player_list.push(test_player_two_node)

        self.player_list.unshift()

        self.assertEqual(len(self.player_list), 1)
        self.assertEqual(self.player_list.head.key, 456)

        self.player_list.unshift()

        self.assertEqual(self.player_list.is_empty, True)
        self.assertEqual(self.player_list.head, None)
        self.assertEqual(self.player_list.unshift(), 'The list is empty.')

    def test_remove_item_from_tail(self):
        test_player_one = Player(123, 'Joe')
        test_player_one_node = PlayerNode(test_player_one)

        test_player_two = Player(456, 'Smith')
        test_player_two_node = PlayerNode(test_player_two)

        test_player_three = Player(789, 'Brett')
        test_player_three_node = PlayerNode(test_player_three)

        self.player_list.push(test_player_one_node)
        self.player_list.push(test_player_two_node)
        self.player_list.push(test_player_three_node)

        self.player_list.pop()

        self.assertEqual(len(self.player_list), 2)
        self.assertEqual(self.player_list.tail.key, 456)

        self.player_list.pop()

        self.assertEqual(len(self.player_list), 1)
        self.assertEqual(self.player_list.tail, None)
        self.assertEqual(self.player_list.head.key, 123)

        self.player_list.pop()

        self.assertEqual(self.player_list.is_empty, True)
        self.assertEqual(self.player_list.pop(), 'The list is empty.')