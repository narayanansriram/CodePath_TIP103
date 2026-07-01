# Imagine a linked list used to track the order in which Mario Kart players finished in a race. The head of the list represents the first place finisher, and the tail or last node in the list represents the last place finisher.

# Given the head of the list, write a function last_place() that returns the player_name of the player that finished last in the race. If the list is empty, return None.

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

def last_place(head):
    if not head:
        return None
    while head.next:
        head = head.next
    return head.player_name
    


# Example Usage:

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(last_place(racers1)) 
print(last_place(racers2)) 
print(last_place(None))

# Example Output:

# Daisy
# Mario
# None
