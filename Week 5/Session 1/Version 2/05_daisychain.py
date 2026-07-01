# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Connect the provided node instances below to create the linked list daisy -> peach -> luigi -> mario.

# A function print_linked_list() which accepts the head, or first element, of a linked list has also been provided for testing purposes.

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

daisy = Node("Daisy")
peach = Node("Peach")
luigi = Node("Luigi")
mario = Node("Mario")
daisy.next = peach
peach.next = luigi
luigi.next = mario
# Add code here to link the above nodes

# Example Usage:

print_linked_list(daisy)

# Example Output:

# Daisy -> Peach -> Luigi -> Mario
