import unittest
from app.player_hashmap import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        self.player_hashmap = PlayerHashMap()

    def test_add_player_to_empty_hashmap(self):
        self.player_hashmap['123'] = 'John'
        self.assertEqual(len(self.player_hashmap), 1)

    def test_add_player_to_non_empty_hashmap(self):
        self.player_hashmap['456'] = 'Jane'
        self.assertEqual(len(self.player_hashmap), 1)

        self.player_hashmap['789'] = 'Jeremy'
        self.assertEqual(len(self.player_hashmap), 2)

    def test_update_player_with_same_key(self):
        self.player_hashmap['123'] = 'John'
        self.player_hashmap['123'] = 'Aaron'

        self.assertEqual(len(self.player_hashmap), 1)

        # Add another test to verify that name has changed from John to Aaron.

    def test_get_index_method(self):
        self.player_hashmap['123'] = 'John'
        self.assertEqual(self.player_hashmap.get_index('123'), 7)

    def test_add_to_same_player_list_if_hashes_are_equal(self):
        self.player_hashmap['123'] = 'John'
        self.player_hashmap['456'] = 'Jude'

        self.assertEqual(len(self.player_hashmap), 2)

    def test_delete_item_from_hashmap(self):
        self.player_hashmap['123'] = 'John'
        self.player_hashmap['456'] = 'Jude'
        self.player_hashmap['888'] = 'Heng'
        self.player_hashmap['923'] = 'Joe'

        del self.player_hashmap['456']
        self.assertEqual(len(self.player_hashmap), 3)

        del self.player_hashmap['123']
        self.assertEqual(len(self.player_hashmap), 2)

        del self.player_hashmap['888']
        self.assertEqual(len(self.player_hashmap), 1)

        del self.player_hashmap['923']
        self.assertEqual(len(self.player_hashmap), 0)

    def test_delete_item_from_empty_hashmap(self):
        with self.assertRaises(ValueError):
            del self.player_hashmap['123']