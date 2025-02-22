import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(123, 'John')

    def test_user_id(self):
        self.assertEqual(self.player.uid, 123)

    def test_user_name(self):
        self.assertEqual(self.player.name, 'John')