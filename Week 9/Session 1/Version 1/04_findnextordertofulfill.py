# You store each customer order at your bakery in a binary tree where each node represents a different order. Each level of the tree represents a different day's orders. Given the root of a binary tree order_tree and an TreeNode object order representing the order you are currently fulfilling, return the next order to fulfill that day. The next order to fulfill is the nearest node on the same level. Return None if order is the last order of the day (rightmost node of the level).

# Note: Because we must pass in a reference to a node in the tree, you cannot use the build_tree() function for testing. You must manually create the tree.

class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

from collections import deque
def find_next_order(order_tree, order):
    q = deque()
    q.append(order_tree)
    while q:
        prev = None
        for _ in range(len(q)):
            curr = q.popleft()
            # print(curr.val,prev.val if prev else None)
            # print(curr.val)
            if prev == order:
                return curr
            prev = curr
            if curr.left:
                q.append((curr.left))
            if curr.right:
                q.append((curr.right))
    return TreeNode(None)

# Example Usage:

"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)
print(next_order1.val)
print(next_order2.val)

# Example Output:

# Eclair
# None
