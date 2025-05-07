from app.player import Player
from app.player_bst import PlayerBST

# Manual testing

test = PlayerBST()
player_one = Player('1', 'John', 10)
player_two = Player('2', 'Jack', 20)
player_three = Player('3', 'Joe', 30)
player_four = Player('4', 'Koala', 40)
player_five = Player('5', 'Aaron', 50)
player_six = Player('6', 'Jackson', 60)
player_seven = Player('7', 'Lauren', 70)

players = [player_one, player_two, player_three, player_four, player_five, player_six, player_seven]

for p in players:
    test.insert(p)

print(test)
test.balance()
print(test)