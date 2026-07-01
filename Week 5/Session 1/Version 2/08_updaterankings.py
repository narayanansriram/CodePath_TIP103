# A 1-indexed linked list is used to track the overall standings of players in a Mario Kart tournament. Write a function increment_rank() that accepts the head of the list and an index target. The function should swap the order of the nodes at index target and index target - 1. If target is the first node in the list, return the original list. Otherwise, return the head of the modified list.

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

def increment_rank(head, target):
    if not head or target <=1:
        return head
    previi = None
    prev = None
    curr = head

    for _ in range(target-1):
        previi = prev
        prev = curr
        curr = curr.next
    #     print(prev.player_name)
    # print("---")
    previi.next = curr
    temp = prev.next
    prev.next = curr.next
    curr.next = temp
    curr.next = prev
    prev = curr

    return head

# Example Usage:

# Example 1:
racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1)) 

# Example Output:

# Mario -> Luigi -> Peach -> Daisy
# Mario -> Luigi
# None
