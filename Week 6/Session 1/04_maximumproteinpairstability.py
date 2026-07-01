# You are analyzing the stability of protein chains, which are represented by a singly linked list where each node contains an integer stability value. The chain has an even number of nodes, and for each node i (0-indexed), its "twin" is defined as node (n-1-i), where n is the length of the linked list.

# Write a function max_protein_pair_stability() that accepts the head of a linked list, and determines the maximum "twin stability sum," which is the sum of the stability values of a node and its twin.

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

def max_protein_pair_stability(head):
    fast = head
    slow = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    maxSum = 0
    while prev and head:
        maxSum = max(maxSum,prev.value+head.value) 
        prev = prev.next
        head = head.next
    return maxSum
    

# Example Usage:

# Example 1 Linked list head1

# Example 2 Linked list head2

head1 = Node(5, Node(4, Node(2, Node(1))))
head2 = Node(4, Node(2, Node(2, Node(3))))

print(max_protein_pair_stability(head1))
print(max_protein_pair_stability(head2))

# Example Output:

# 6
# Example 1 Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 

# 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
