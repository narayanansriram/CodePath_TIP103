# Atlanteans are planning multiple missions to explore the deep ocean, and each mission has a priority level represented as a node in a linked list. You are given the heads of two sorted linked lists, mission1 and mission2, where each node represents a mission with its priority level.

# Implement a recursive function merge_missions() which merges these two mission lists into one sorted list, ensuring that the combined list maintains the correct order of priorities. The merged list should be made by splicing together the nodes from the first two lists.

# Return the head of the merged mission linked list.

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

def merge_missions(mission1, mission2):
    dummy = Node(0)
    head = dummy
    while mission1 and mission2:
        if mission1.value<mission2.value:
            head.next = mission1
            mission1 = mission1.next
            head = head.next
        else:
            head.next = mission2
            mission2 = mission2.next
            head = head.next
    while mission1:
        head.next = mission1
        mission1 = mission1.next
        head = head.next
    while mission2:
        head.next = mission2
        mission2 = mission2.next
        head = head.next
    return dummy.next


# Example Usage:

mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))

# 1 -> 1 -> 2 -> 3 -> 4 -> 4
