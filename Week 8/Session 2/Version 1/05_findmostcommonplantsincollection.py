# You have a vast plant collection and want to know which plants you own the most of. Given the root of a BST with duplicates where each node is a plant in your collection, return a list with the name(s) (val) of the most frequently occurring plant(s) in your collection. If multiple plants tie for the most frequently occuring plant, you may return them in any order.

# Assume your BST organizes plants alphabetically by name and follows the following rules:

#     The left subtree of a node contains only nodes with values less than or equal to the node's value
#     The right subtree of a node contains only nodes with values greater than or equal to the node's value.
#     Both the left and right subtrees must also be BSTs.

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
from collections import defaultdict,deque
def find_most_common(root):
    h = defaultdict(int)
    q = deque()
    q.append(root)
    while q:
        lenLev = len(q)
        for _ in range(lenLev):
            root = q.popleft()
            h[root.val]+=1
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
    c = defaultdict(list)
    for k,v in h.items():
        c[v].append(k)
    f = sorted(c.items(),reverse=True)
    # print(f)
    return f[0][1]

# Example Usage:

"""
    Hoya
      \ 
      Pothos
      /
    Pothos
"""

# Using build_tree() function at top of page
values = ["Hoya", None, "Pothos", "Pothos"]
collection1 = build_tree(values)

"""
      Hoya
    /      \ 
  Aloe    Pothos
  /        /
 Aloe   Pothos
"""
values = ["Hoya", "Aloe", "Pothos", "Aloe", None, "Pothos"]
collection2 = build_tree(values)

print(find_most_common(collection1))
print(find_most_common(collection2))

# Example Output:

# ['Pothos']
# ['Aloe', 'Pothos']
