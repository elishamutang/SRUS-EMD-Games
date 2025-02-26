import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

class TestPlayerList(unittest.TestCase):

    def setUp(self):
        self.player_list = PlayerList()

        test_player_one = Player(123, 'Joe')
        self.test_player_one_node = PlayerNode(test_player_one)

        test_player_two = Player(456, 'Smith')
        self.test_player_two_node = PlayerNode(test_player_two)

        test_player_three = Player(789, 'Brett')
        self.test_player_three_node = PlayerNode(test_player_three)

        test_player_four = Player(431, 'John')
        self.test_player_four_node = PlayerNode(test_player_four)

        test_player_five = Player(856, 'Sarah')
        self.test_player_five_node = PlayerNode(test_player_five)

        test_player_six = Player(223, 'Oli')
        self.test_player_six_node = PlayerNode(test_player_six)

    def test_add_to_head_on_empty_list(self):
        self.player_list.shift(self.test_player_one_node)

        self.assertEqual(self.player_list.is_empty, False)
        self.assertEqual(self.player_list.head.key, self.test_player_one_node.key)
        self.assertEqual(len(self.player_list), 1)

    def test_add_to_head_on_non_empty_list(self):
        self.player_list.shift(self.test_player_one_node)
        self.player_list.shift(self.test_player_two_node)

        self.assertEqual(len(self.player_list), 2)
        self.assertEqual(self.player_list.head.key, 456)
        self.assertEqual(self.player_list.tail.key, 123)

    def test_add_to_tail_on_empty_list(self):
        self.player_list.push(self.test_player_one_node)

        self.assertEqual(self.player_list.is_empty, False)
        self.assertEqual(self.player_list.head.key, 123)

    def test_add_to_tail_on_non_empty_list(self):
        self.player_list.push(self.test_player_one_node)
        self.player_list.push(self.test_player_two_node)

        self.assertEqual(len(self.player_list), 2)
        self.assertEqual(self.player_list.tail.key, 456)

    def test_remove_item_from_head(self):
        self.player_list.push(self.test_player_one_node)
        self.player_list.push(self.test_player_two_node)

        self.player_list.unshift()

        self.assertEqual(len(self.player_list), 1)
        self.assertEqual(self.player_list.head.key, 456)

        self.player_list.unshift()

        self.assertEqual(self.player_list.is_empty, True)
        self.assertEqual(self.player_list.head, None)

        with self.assertRaises(IndexError):
            self.player_list.unshift()

    def test_remove_item_from_tail(self):
        self.player_list.push(self.test_player_one_node)
        self.player_list.push(self.test_player_two_node)
        self.player_list.push(self.test_player_three_node)

        self.player_list.pop()

        self.assertEqual(len(self.player_list), 2)
        self.assertEqual(self.player_list.tail.key, 456)

        self.player_list.pop()

        self.assertEqual(len(self.player_list), 1)
        self.assertEqual(self.player_list.head.key, 123)

        self.player_list.pop()

        self.assertEqual(self.player_list.tail, None)
        self.assertEqual(self.player_list.is_empty, True)

        with self.assertRaises(IndexError):
            self.player_list.pop()

