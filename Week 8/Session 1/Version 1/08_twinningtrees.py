# Given the roots of two trees root1 and root2, return True if the trees have identical structures and values and False otherwise.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    left = is_identical(root1.left,root2.left)
    right = is_identical(root1.right, root2.right)
    return left and right and root1.val == root2.val 

# Example Usage:

"""
      1                1
     / \              / \
    2   3            2   3  
"""
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

"""
      1                1
     /                  \
    2                    2  
"""

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, TreeNode(2))
print(is_identical(root3, root4))
root4 = TreeNode(1, TreeNode(1))
print(is_identical(root3, root4))
# Example Output:

True
False
