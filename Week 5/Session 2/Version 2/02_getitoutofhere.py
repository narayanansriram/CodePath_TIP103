# The following code incorrectly implements the function remove_by_value(). When implemented correctly, remove_by_value() accepts the head of a singly linked list and a value val, and removes the first node in the linked list with the value val. It should return the head of the modified list.

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against, and use print statements, print_linked_list(), and the stack trace to identify and fix any bug(s) so that the function correctly removes a node by value from the list.

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Function with a bug!
def remove_by_value(head, val):
    if not head:
        return None
    if head.value == val:
        return head.next  

    current = head
    while current.next:
        if current.next.value == val:
            current.next = current.next.next  
            return head  
        current = current.next

    return head

# Example Usage:

head = Node("Daisy", Node("Mario", Node("Waluigi", Node("Baby Peach"))))

print_linked_list(remove_by_value(head, "Waluigi"))

# Expected Output:

# Daisy -> Mario -> Baby Peach
