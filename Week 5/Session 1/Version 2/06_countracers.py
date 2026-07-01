# Imagine a linked list used to track the order in which Mario Kart players finished in a race. The head of the list represents the first place finisher, and the tail or last node in the list represents the last place finisher.

# Write a function count_racers() that accepts the head of the list and returns the number of players who participated in the race.

class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def count_racers(head):
    count = 0
    while head:
        count+=1
        head = head.next
    return count

# Example Usage:

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(count_racers(racers1))
print(count_racers(racers2))
print(count_racers(None))

# Example Output:

# 4
# 1
# 0
