# Given the head of a singly linked list, reverse the list, and return the head of the reversed list. You must reverse the list in place. Return the head of the reversed list.

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


def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


# Example Usage:

kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))

print_linked_list(reverse(kart_choices))

# Example Output:

# Pirahna Prowler -> Wild Wing -> Bullet Bike
