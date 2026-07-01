# The Player class has been updated below with a new attribute ahead to represent the player currently directly ahead of them in the race.

# Write a function get_place() that accepts a Player object my_player and returns their current place number in the race.

class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

def get_place(my_player):
    curr = my_player
    count = 0
    while curr:
        count+=1
        curr = curr.ahead

    return count

# Example Usage:

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
player2_rank = get_place(peach)
player3_rank = get_place(mario)

print(player1_rank)
print(player2_rank)
print(player3_rank)

# Example Output:

# 3
# 1
# 2
