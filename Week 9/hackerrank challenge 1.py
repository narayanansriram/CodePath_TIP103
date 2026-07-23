def calculate_depth(root):
    if not root:
        return 0
    left_depth = calculate_depth(root.left)
    right_depth = calculate_depth(root.right)
    return max(left_depth, right_depth) + 1
"""Yes, O(n) is correct — let's confirm the reasoning.
Every node in the tree triggers exactly one call to calculate_depth (via the recursive calls on .left and .right), and each call does O(1) work beyond the recursive calls themselves (just a comparison and an addition). Since there are n nodes total, and each is visited exactly once, the total time is O(n).
Quick follow-up, since we've been building this habit throughout our conversation: what about space complexity? Think about the call stack — does it depend on whether the tree is balanced or skewed, the same way we discussed with sum_tree_levels and is_complete earlier?"""

def find_all_paths(root):
    def dfs(node,path,paths):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            paths.append(list(path))
        else:
            dfs(node.left,path,paths)
            dfs(node.right,path,paths)
        path.pop()
    paths = []
    dfs(root, [], paths)
    return paths

# space complexity is O(n)

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def mystery_functions(root):
    if not root:
        return 0
    return max(mystery_functions(root.left), mystery_functions(root.right)) + 1

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)
output = mystery_functions(root)
print(output)

# Find the bug
def is_balanced(root):
    def check_balance(node):
        if not node:
            return 0
        
        left_height = check_balance(node.left)
        right_height = check_balance(node.right)
        
        if left_height == -1 or right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) 
    

    return check_balance(root) != -1