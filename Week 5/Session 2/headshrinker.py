class Node:
    def __init__(self,value,next_node=None,prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node
def mystery_function(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    return current

head = Node(1,Node(2,Node(3)))

head = mystery_function(head)

result = []
while head:
    result.append(head.value)
    head = head.next
print(result)