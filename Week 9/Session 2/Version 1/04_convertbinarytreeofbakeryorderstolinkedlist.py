# You've been storing your bakery's orders in a binary tree where each node represents an order for a while now, but are wondering whether a new system would work better for you. You want to try storing orders in a linked list instead.

# Given the root of a binary tree orders, flatten the tree into a 'linked list'.

#     The 'linked list' should use the same TreeNode class where the right child points to the next node in the list and the left child pointer is always None.
#     The 'linked list' should be in the same order as a preorder traversal of the binary tree.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.
from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def flatten_orders(orders):
    dummy = TreeNode(0)
    head = dummy
    def preorder(root):
        if not root:
            return
        nonlocal head
        head.right = TreeNode(root.val)
        head = head.right
        preorder(root.left)
        preorder(root.right)
    preorder(orders)
    return dummy.right

# Example Usage:

"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \           \
Cake     Pie         Blondies
"""
# Using build_tree() function included at the top of page
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
orders = build_tree(items)

# Using print_tree() function included at the top of page
print_tree(flatten_orders(orders))

# Example Output:

# ['Croissant', None, 'Cupcake', None, 'Cake', None, 'Pie', None, 'Bagel', None, 'Blondies']
# Explanation:
# 'Linked List':
# Croissant
#     \
#    Cupcake
#        \
#        Cake
#          \
#          Pie
#            \
#            Bagel
#              \
#             Blondies
