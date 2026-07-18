# You have a Pothos plant represented as a binary tree, where each node in the tree represents a segment of the plant. Given the root of your pothos and a value target, you want to delete all leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted. You should continue deleting nodes until you cannot.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
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

def prune(root, target):
    def helper(root):
        if not root:
            return 
        if root.left == None and root.right == None and root.val == target:
            nonlocal cut
            cut = True
            return None
        root.left = helper(root.left)
        root.right = helper(root.right)
        return root
    while True:
        cut = False
        helper(root)
        if cut == False:
            break
    # cut = 0
    # helper(root)
    return root

# Example Usage 1:

# 'pothos1' after each set of deletions

"""
         Healthy
        /       \
     Dying    Healthy
     /          /  \
   Dying     Dying  New Growth
"""

# Using build_tree() function at the top of the page
values = ["Healthy", "Dying", "Healthy", "Dying", None, "Dying", "New Growth"]
pothos1 = build_tree(values)

# Using print_tree() function at the top of the page
print_tree(prune(pothos1, "Dying"))

# Example Output:

# ['Healthy', None, 'Healthy', None, 'New Growth']
# Explanation:
# Modified Tree:
# Healthy
#      \
#      Healthy
#         \
#         New Growth

# Example Usage 2:

"""
      Healthy
     /        \
   Aphids     Aphids
   /     \
 Aphids New Growth 
"""

values = ["Healthy", "Aphids", "Aphids", "Aphids", "New Growth"]
pothos2 = build_tree(values)

print_tree(prune(pothos2, "Aphids"))

# Example Output 2:

# ['Healthy', 'Aphids', None, None, 'New Growth']

# Explanation:
# Modified Tree:
#     Healthy
#     /
# Aphids
#     \
#     New Growth
