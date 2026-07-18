# You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node. If there is no right child, return only the root node value (the rightmost path in this case is just the root node).

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque
def right_vine(root):
    q = deque()
    q.append(root)
    r = []
    while q:
        levLen = len(q)
        ex = None
        for _ in range(levLen):
            root = q.popleft()
            ex = root
            # if root.left:
            #     q.append(root.left)
            if root.right:
                q.append(root.right)
        r.append(ex.val)
    return r


     

# Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

# Example Output:

# ['Root', 'Node2', 'Leaf3']
# ['Root']
