# You have the root of a binary search tree orders, where each node in the tree represents an order and each node's value represents the number of cupcakes the customer ordered. Convert the tree to a 'larger order tree' such that the value of each node in tree is equal to its original value plus the sum of all node values greater than it.

# As a reminder a BST satisfies the following constraints:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
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

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

# Example Usage:

"""
          1
        /   \
       2     3
      /     / \
     4     5   6
"""

# root = Node(1, Node(2, Node(4)), Node(3, Node(5), Node(6)))

# print_tree(root)
# print_tree(None)

# Example Output:

# [1, 2, 3, 4, None, 5, 6]
# 'Empty'

def larger_order_tree(orders):
    total = 0
    def inorder_total(orders):
        if not orders:
            return
        inorder_total(orders.left)
        nonlocal total
        total+=orders.val
        inorder_total(orders.right)
    def larger_tree(orders):
        if not orders:
            return
        larger_tree(orders.left)
        nonlocal total
        temp = orders.val
        orders.val = total
        total -= temp
        larger_tree(orders.right)
    inorder_total(orders)
    larger_tree(orders)
    return orders
    

# Examples Usage:

# Example 'orders' tree with both original node vlaue and larger order value listed

"""
         4
       /   \
      /     \
     1       6
    / \     / \
   0   2   5   7
        \       \
         3       8   
"""
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))

# Example Output:

# [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
# Explanation:
# Larger Order Tree:
#         30
#        /   \
#       /     \
#      36     21
#     / \     / \
#    36  35  26  15
#          \       \
#          33       8   
