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

from collections import deque
def remove_plant(root, name):
    
    if not root:
        return None
    if name < root.val:
        root.left = remove_plant(root.left, name)
    elif name > root.val:
        root.right = remove_plant(root.right, name)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        pred = root.left
        if not pred.right:
            pred.right = root.right
            return pred
        parent = root.left
        while parent.right.right:
            parent = parent.right
        pred = parent.right
        parent.right = pred.left
        pred.left = root.left
        pred.right = root.right
        return pred
    return root    


# Example Usage:

"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))

# Example Output:

['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']

# Explanation:
# The resulting tree structure:
#              Money Tree
#             /         \
#           Hoya       Orchid
#               \          \
#               Ivy      ZZ Plant

# Build this tree:
#        Root
#       /    \
#      A      Target
#            /      \
#          Mid        Right2
#         /
#      Left2
#         \
#        Left2Right
left2right = TreeNode('Left2Right')
left2 = TreeNode('Left2', None, left2right)
right2 = TreeNode('Right2')
mid = TreeNode('Mid', left2, None)
target = TreeNode('Target', mid, right2)
a = TreeNode('A')
root = TreeNode('Root', a, target)

print_tree(root)
result = remove_plant(root, 'Target')
print_tree(result)

# Root
# ├── A
# └── Left2
#     ├── Mid
#     │   └── Left2Right
#     └── Right2
# ['Root', 'A', 'Left2', None, None, 'Mid', 'Right2', 'Left2Right']