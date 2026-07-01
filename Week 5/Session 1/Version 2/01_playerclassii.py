# A class constructor is a special method or function that is used to create and initialize a new object from a class. Define the class constructor __init__() for a new class Player that represents Mario Kart players. The constructor accepts two required arguments: strings character and kart. The constructor should define three properties for a Player:

#     character, a string initialized to the argument character
#     kart, a string initialized to the argument kart
#     items, a list initialized to an empty list

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

# Example Usage:

player_one = Player("Yoshi", "Super Blooper")
print(player_one.character)
print(player_one.kart) 
print(player_one.items)

# Example Output:

# Yoshi
# Super Blooper
# []
