# You've accumulated too many plants, and need to split up your collection. Given the root of a BST collection where each node represents a plant in your collection and a value target, split the tree into two subtrees where the first subtree has node values that are lexicographically (alphabetically) smaller than or equal to target and the second subtree has all nodes that are greater than target. It is not necessarily the case that the collection contains a plant (node) with value target.

# Additionally, most of the structure of the original tree should remain. Formally for any child plant c with parent p in the original collection, if they are both in the same subtree/subcollection after teh split, then plant c should still have the parent p.

# Return an array of the two root nodes of the two subtrees in order.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

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
def split_collection(collection, target):
    newRoot = None
    def helper(root,prev):
        if not root:
            return
        nonlocal newRoot
        if root.val == target:
            # print(f"found --> parent is {prev.val}")
            temp = root.right
            root.right = None
            nonlocal newRoot
            newRoot = root
            return temp
        # print(root.val)
        root.left = helper(root.left,root)
        root.right = helper(root.right,root)
        return root
    helper(collection,None)
    # print_tree(newRoot)
    return (collection,newRoot)



# Example Usage:

# Example input BST 'collection'

"""
              Money Tree
             /         \
           Hoya        Pilea
           /   \        /   \
        Aloe   Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of the page
values = ["Money Tree", "Hoya", "Pilea", "Aloe", "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of the page
left, right = split_collection(collection, "Hoya")
print_tree(left)
print_tree(right)

# Example Output:

# Example Left and Right Output Subtrees for 'collection'

# ['Hoya', 'Aloe']
# ['Money Tree', 'Ivy', 'Pilea', None, None, 'Orchid', 'ZZ Plant']

# Explanation:
# Left Subtree:
#    Hoya
#    /
# Aloe

# Right Subtree:
#     Money Tree
#     /       \
#    Ivy     Pilea
#           /     \
#        Orchid  ZZ Plant
