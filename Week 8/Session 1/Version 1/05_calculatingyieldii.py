class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if not root.left and not root.right:
        return root
    left = calculate_yield(root.left)
    right = calculate_yield(root.right)
    if root.val == "+":
        return left+right
    elif root.val == "-":
        return left.val-right.val
    elif root.val == "*":
        return left.val*right.val
    elif root.val == "/":
        return left.val/right.val

# Example Usage:

"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))

# Example Output:

# 22
# Explanation:
# - 4 - 2 = 2
# - 10 * 2 = 20
# - 2 + 20 = 22
