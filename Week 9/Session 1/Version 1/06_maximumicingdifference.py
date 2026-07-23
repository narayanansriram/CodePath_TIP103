# In your bakery, you're planning a display of cupcakes where each cupcake is represented by a node in a binary tree. The sweetness level of the icing on each cupcake is stored in the node's value. You want to identify the maximum icing difference between any two cupcakes where one cupcake is an ancestor of the other in the display.

# Given the root of a binary tree representing the cupcake display, find the maximum value v for which there exist different cupcakes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A cupcake a is an ancestor of b if either any child of a is equal to b, or any child of a is an ancestor of b.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
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

from collections import deque
def max_icing_difference(root):
    maxDiff = float('-inf')
    def inorder(root,maxSeen):
        if not root:
            return
        maxSeen = max(maxSeen,root.val)
        nonlocal maxDiff
        maxDiff = max(maxDiff,abs(maxSeen-root.val))
        inorder(root.left,maxSeen)
        inorder(root.right,maxSeen)
    inorder(root,root.val)
    return maxDiff

# Example Usage:

"""
            8
           /  \
         3     10
        / \      \
       1   6     14
          /  \    /
         4    7  13
"""

# Using build_tree() function included at top of page
sweetness_levels = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
display = build_tree(sweetness_levels)

print(max_icing_difference(display))

# Example Output:

# 7
# Explanation: The maximum icing difference is between the root cupcake (8) and a descendant with
# sweetness level 1, yielding a difference of |8 - 1| = 7.
