# Your bakery's inventory is organized in a binary tree where each node represents a different bakery item. To make it easier for staff to locate items, you want to create a vertical display of the inventory. The vertical order traversal should be organized column by column, from left to right.

# If two items are in the same row and column, they should be listed from left to right, just as they appear in the inventory.

# Given the root of the binary tree representing the inventory, return a list of lists with the vertical order traversal of the bakery items. Each inner list should represent the ith column in the inventory tree, and each inner list's elements should include the values of each bakery item in that column.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

from collections import deque, defaultdict
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

def vertical_inventory_display(root):
    vot = defaultdict(list)
    q = deque()
    q.append((root,0))
    while q:
        for _ in range(len(q)):
            root,num = q.popleft()
            vot[num].append(root.val)
            if root.left:
                q.append((root.left,num-1))
            if root.right:
                q.append((root.right,num+1))
    result = sorted(vot.items(), key = lambda x:x[0])
    return [i[1] for i in result]

# Example Usage 1:

# 'inventory1' example tree with columns color coded

"""
         Bread
       /       \
   Croissant    Donut
                /   \
             Bagel Tart
"""
# Using build_tree() function included at the top of the page
inventory_items = ["Bread", "Croissant", "Donut", None, None, "Bagel", "Tart"]
inventory1 = build_tree(inventory_items)

print(vertical_inventory_display(inventory1))  

# Example Output 1:

[['Croissant'], ['Bread', 'Bagel'], ['Donut'], ['Tart']]


# Example Usage 2:

# 'inventory2' example tree with columns color coded

"""
         Bread
       /       \
   Croissant    Donut
   /    \        /   \
Muffin  Scone Bagel Tart
        /       \
      Pie     Cake
"""  
inventory_items = ["Bread", "Croissant", "Donut", "Muffin", "Scone", "Bagel", "Tart", None, None, "Pie", None, None, "Cake", None, None]
inventory2 = build_tree(inventory_items)

print(vertical_inventory_display(inventory2))  

# Example Output 2:

# [['Muffin'], ['Croissant', 'Pie'], ['Bread', 'Scone', 'Bagel'], ['Donut', 'Cake'], ['Tart']]
