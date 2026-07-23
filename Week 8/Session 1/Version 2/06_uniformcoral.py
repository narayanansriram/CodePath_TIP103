# Triton is looking for the perfect piece of coral to gift his mother, Amphitrite, for her birthday. Given the root of a binary tree representing a coral structure, write a function is_uniform() that evaluates the quality of the coral. The function should return True if each node in the coral tree has the same value and False otherwise.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque
def is_uniform(root):
    q = deque()
    q.append(root)
    prev = None
    res = []
    while q:
        lev = []
        for _ in range(len(q)):
            root = q.popleft()
            lev.append(root.val)
            if not prev:
                prev = root.val
            elif prev != root.val:
                return False
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        res.append(lev)
    print(res)
    return True

# Example Usage:

"""
         1
        / \
       1   1
      / \      
     1   1 
"""
coral = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1))


"""
   1
  / \
 2   1
"""
coral2 = TreeNode(1, TreeNode(2), TreeNode(1))

print(is_uniform(coral))
print(is_uniform(coral2))

# Example Output:

# True
# False
