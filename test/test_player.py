import unittest
import random
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

        self.assertTrue(bob < alice)

    def test_sort_players_using_custom_sorting_algorithm(self):
        players = [Player(player_id='01', name='Alice', score=10),
                   Player(player_id='02', name='Bob', score=5),
                   Player(player_id='03', name='Charlie', score=15)]

        sorted_players = Player.sort(players)

        manually_sorted_players = [Player(player_id='03', name='Charlie', score=15),
                                   Player(player_id='01', name='Alice', score=10),
                                   Player(player_id='02', name='Bob', score=5)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_sort_players_using_custom_sorting_algorithm_at_scale(self):
        players = [Player(player_id=f"{i:03}", name=f"Player a{i}", score=random.randint(0, 1000)) for i in range(1000)]

        sorted_players_using_sorted = sorted(players, reverse=True)
        print(sorted_players_using_sorted)
        sorted_players_using_custom_sort = Player.sort(players)
        print(sorted_players_using_custom_sort)

        self.assertListEqual(sorted_players_using_sorted, sorted_players_using_custom_sort)

    def test_sort_players_for_sorted_list_of_players(self):
        players = [Player(player_id=f"{i:03}", name=f"Player {i}", score=random.randint(0, 1000)) for i in range(1000)]

        sorted_players = sorted(players, reverse=True)
        print(sorted_players)
        sorted_players_using_custom_sort = Player.sort(sorted_players)
        print(sorted_players_using_custom_sort)

        self.assertListEqual(sorted_players, sorted_players_using_custom_sort)