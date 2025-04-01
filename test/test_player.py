import unittest
from app.player import Player


class TestPlayerSort(unittest.TestCase):

    def test_sort_players(self):
        players = [Player(player_id='01', name='Alice', score=10),
                   Player(player_id='02', name='Bob', score=5),
                   Player(player_id='03', name='Charlie', score=15)]

        sorted_players = sorted(players)

        manually_sorted_players = [Player(player_id='02', name='Bob', score=5),
                                   Player(player_id='01', name='Alice', score=10),
                                   Player(player_id='03', name='Charlie', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        alice = Player(player_id='01', name='Alice', score=10)
        bob = Player(player_id='02', name='Bob', score=5)

        self.assertTrue(alice.score < bob.score)
