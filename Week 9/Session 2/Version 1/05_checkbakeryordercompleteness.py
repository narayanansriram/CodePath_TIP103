# You have a customer order you are currently making stored in a binary tree where each node represents a different item in the order. Given the root of the order you are fulfilling, return True if the order is complete and False otherwise.

# An order is complete if every level of the tree, except possibly the last, is completely filled with items (nodes), and all items in the last level are as far left as possible. It can have between 1 and 2^h items inclusive at the last level h where levels are 0-indexed.

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

def is_complete(root):
    q = deque()
    q.append(root)
    h = 0
    while q:
        lev = []
        for _ in range(len(q)):
            root = q.popleft()
            if not root:
                lev.append(None)
                continue
            lev.append(root.val)
            if root.left:
                q.append(root.left)
            else:
                q.append(None)
            if root.right:
                q.append(root.right)
            else:
                q.append(None)
        if all([i==None for i in lev]):
            break
        for i in range(1,len(lev)):
            if lev[i] and not lev[i-1]:
                return False
    return True

# Example Usage:

"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \      /
Cake     Pie  Blondies
"""
# Using build_tree() function included at the top of page
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", "Blondies"]
order1 = build_tree(items)

"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \           \
Cake     Pie         Blondies
"""
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
order2 = build_tree(items)

print(is_complete(order1))
print(is_complete(order2))

# Example Output:

# True
# False
