# You are given the root of a binary tree representing possible route through a system of sea caves. You recall that so long as you take the leftmost branch at every fork in the route, you'll find your way back home. Write a function leftmost_path() that returns an array with the value of each node in the leftmost path. If there is no left child, return only the root node value (the leftmost path in this case is just the root node).

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    result = []
    while root:
        result.append(root.val)
        root = root.left
    return result

# Example Usage:

"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF  
"""
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  CaveA
      \
      CaveB
        \
        CaveC  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path(system_a))
print(leftmost_path(system_b))

# Example Output:

# ['CaveA', 'CaveB', 'CaveD']
# ['CaveA']
