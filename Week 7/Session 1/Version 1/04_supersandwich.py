# A regular at the deli has requested a new order made by merging two different sandwiches on the menu together. Given the heads of two linked lists sandwich_a and sandwich_b where each node in the lists contains a sandwich layer, write a recursive function merge_orders() that merges the two sandwiches together in the pattern:

# a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

# Return the head of the merged sandwich.

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

def merge_orders(sandwich_a, sandwich_b):
    def merger(c,a,b):
        if a and not b:
            c.next = a
            return
        if b and not a:
            c.next = b
            return
        if a and b:
            # print(a.value,b.value)
            next_a = a.next
            next_b = b.next
            c.next = a#Node(a.value)
            c = c.next
            c.next = b#Node(b.value)
            c = c.next
            merger(c,next_a,next_b)
        return c
        
    dummyNode = Node(0)
    merger(dummyNode,sandwich_a,sandwich_b)
    return dummyNode.next

# Example Usage:

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
print_linked_list(merge_orders(sandwich_a, sandwich_c))

# Example Output:

# Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
# Bacon -> Bread -> Lettuce -> Tomato
