# You have a cupcake display represented by a binary tree where each node represents a different cupcake in the display and each node value represents the flavor of the cupcake. Given the root of the binary tree display a string flavor and an integer depth, insert a row of nodes with value flavor at the given depth depth.

# Note that the root node has depth 1.

# The inserting rule is:

#     Given the integer depth, for each existing tree node cur at the depth depth - 1, create two cupcakes with value flavor as cur's left subtree root and right subtree root.
#     cur's original left subtree should be the left subtree of the new left subtree root.
#     cur's original right subtree should be the right subtree of the new right subtree root.
#     If depth == 1 that means there is no depth depth - 1 at all, then create a cupcake with value flavor as the new root of the whole original tree, and the original tree is the new root's left subtree.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
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

def insert_row(display, flavor, depth):
    q = deque()
    root = display
    q.append(root)
    curr = 0
    while q:
        for _ in range(len(q)):
            root = q.popleft()
            if curr == depth - 2:
                newNode = TreeNode(flavor)
                newNode.left = root.left
                root.left = newNode
                newNode2 = TreeNode(flavor)
                newNode2.right = root.right
                root.right = newNode2
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        curr += 1
    return display

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Red Velvet
"""
# Using build_tree() function included at top of page
cupcake_flavors = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Red Velvet"]
display = build_tree(cupcake_flavors)

# Using print_tree() function included at top of page
print_tree(insert_row(display, "Mocha", 3))

# Example Output:

['Chocolate', 'Vanilla', 'Strawberry', 'Mocha', 'Mocha', 'Mocha', 'Mocha', None, None, None, None, 'Chocolate', None, None, 'Red Velvet']
# Explanation:
# Tree with inserted row:
#                    Chocolate
#                    /        \
#              Vanilla        Strawberry
#              /    \         /       \
#           Mocha   Mocha  Mocha     Mocha
#                          /             \
#                       Chocolate       Red Velvet
