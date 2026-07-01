# Players can pick up special items as they race.

# Update the Player class with a new method add_item() that takes in one parameter, item_name.

# The method should validate the item_name.

#     If the item is valid, add item_name to the player’s items attribute.
#     The method does not need to return any values.

# item_name is valid if it has one of the following values: "banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill".

class Player:
    VALID_ITEMS = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def add_item(self, item_name):
        if item_name in self.VALID_ITEMS:
            self.items.append(item_name)
def bub(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def proc_numbers(nums,threshold):
    stk = []
    for num in nums:
        if num < threshold:
            stk.append(num)
        elif num <= 10 and stk:
            stk.pop()
    return stk
print(proc_numbers([3,5,1,9,6,15],8))
# Example Usage:

player_one = Player("Yoshi", "Dolphin Dasher")
print(player_one.items)

player_one.add_item("red shell")
print(player_one.items)

player_one.add_item("super star")
print(player_one.items)

player_one.add_item("super smash")
print(player_one.items)

# Example Output:

[]
['red shell']
['red shell', 'super star']
['red shell', 'super star']
