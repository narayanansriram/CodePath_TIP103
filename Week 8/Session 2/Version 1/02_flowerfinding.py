class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

from collections import deque
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

def find_flower(inventory, name):
    q = deque()
    q.append(inventory)
    while q:
        root = q.pop()
        if root.val == name:
            return True
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
    return False

# Example Usage:

"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

# Example Output:

# True
# False
