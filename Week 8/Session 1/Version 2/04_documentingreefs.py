# You are exploring a vast coral reef system. The reef is represented as a binary tree, where each node corresponds to a specific coral formation. You want to document the reef as you encounter it, starting from the root or main entrance of the reef.

# Write a function explore_reef() that performs a preorder traversal of the reef and returns a list of the names of the coral formations in the order you visited them. In a preorder exploration, you explore the current node first, then the left subtree, and finally the right subtree.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def explore_reef(root):
    if not root:
        return []
    return [root.val] + explore_reef(root.left)+explore_reef(root.right)

# Example Usage:

"""
         CoralA
        /     \
     CoralB  CoralC
     /   \      
 CoralD CoralE  
"""

reef = TreeNode("CoralA", 
                TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")), 
                          TreeNode("CoralC"))

print(explore_reef(reef))

# Example Output:

# ['CoralA', 'CoralB', 'CoralD', 'CoralE', 'CoralC']
