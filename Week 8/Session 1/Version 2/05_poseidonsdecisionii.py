# Poseidon has received advice on an important matter from his council of advisors. Help him evaluate the advice from his council to make a final decision. You are given the advice as the root of a binary tree representing a boolean expression.

#     Leaf nodes have a boolean value of either True or False.
#     Non-leaf nodes have two children and a string value of either AND or OR.

# The evaluation of a node is as follows:

#     If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
#     Otherwise evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.

# Return the boolean result of evaluating the root node.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_decision(root):
    if not root.left and not root.right:
        return root.val
    left = get_decision(root.left)
    right = get_decision(root.right)
    if root.val == "AND":
        return left and right
    if root.val == "OR":
        return left or right

# Example Usage:

"""
        AND
     /      \
   OR       AND
  /  \       /  \
True False True False
"""

root = TreeNode("AND")
root.left = TreeNode("OR")
root.right = TreeNode("AND")
root.left.left = TreeNode(True)
root.left.right = TreeNode(False)
root.right.left = TreeNode(True)
root.right.right = TreeNode(False)
print(get_decision(root))


root = TreeNode("OR")
root.left = TreeNode("OR")
root.right = TreeNode("OR")
root.left.left = TreeNode(True)
root.left.right = TreeNode(False)
root.right.left = TreeNode(True)
root.right.right = TreeNode(False)
print(get_decision(root))
# Example Output:

# False
# Explanation: 
# - Left Subtree Evaluation: True OR False evaluates to True
# - Right Subtree Evaluation: True AND False evaluates to False
# - Root and children Evaluation: True AND False evaluates to False
