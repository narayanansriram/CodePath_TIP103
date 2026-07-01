# On your marks, get set, go! Contestants in the game show are racing along a path that contains a loop, but there's a hidden mini challenge: they aren't told where along the path the loop begins. Given the head of a linked list, path_start where each node represents a point in the path, return the value of the node at the start of the loop. If no loop exists in the path, return None.

# A linked list has a cycle or loop if at some point in the list, the node’s next pointer points back to a previous node in the list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
    slow = path_start
    fast = path_start.next
    while slow!=fast:
        slow = slow.next
        fast = fast.next.next
    fast = slow.next
    while slow!=fast:
        slow=slow.next
        fast=fast.next.next
    return slow.value

# Example Usage:

# Linked list with 4 nodes and a cycle where 4th node points to 2nd node

path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
print(cycle_start(path_start))

# Example Output:

# Point 1
