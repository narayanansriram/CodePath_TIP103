# Given the head of a linked list with integer values and a value val, write a function partition() that partitions the linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(head, val):
    lower = Node(0)
    lCurr = lower
    higher = Node(0)
    hCurr = higher
    while head:
        if head.value<val:
            lCurr.next = head
            lCurr = lCurr.next
        else:
            hCurr.next = head
            hCurr = hCurr.next
        head = head.next
    hCurr.next = None
    lCurr.next = higher.next
    return lower.next

# Example Usage:

head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(head, 3))

# Example Output:

# 1 -> 2 -> 2 -> 4 -> 3 -> 5
# Explanation: There are multiple possible solutions.
# E.g. 2 -> 2 -> 1 -> 5 -> 4 -> 3
