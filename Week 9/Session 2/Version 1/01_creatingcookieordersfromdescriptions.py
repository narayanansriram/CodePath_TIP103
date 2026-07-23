# In your bakery, customer cookie orders are organized in a binary tree, where each node represents a different flavor of cookie ordered by the customers. You are given a 2D integer array descriptions where descriptions[i] = [parent_i, child_i, is_left_i] indicates that parent_i is the parent of child_i in a binary tree of unique flavors.

#     If is_left_i == 1, then child_i is the left child of parent_i.
#     If is_left_i == 0, then child_i is the right child of parent_i.

# Construct the binary tree described by descriptions and return its root.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

from collections import deque, defaultdict
class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

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

def build_cookie_tree(descriptions):
    l = defaultdict(TreeNode)
    root = None
    for parent,child,isLeft in descriptions:
        curr = None
        if parent in l:
            curr = l[parent]
        else:
            curr = TreeNode(parent)
            l[parent] = curr
            if not root:
                root = curr
        childNode = TreeNode(child)
        if isLeft:
            curr.left = childNode
        else:
            curr.right = childNode
        l[child] = childNode
    return root

# Example Usage:

descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))

# Example Output:

['Chocolate Chip', 'Peanut Butter', 'Oatmeal Raisin', 'Sugar']
# Example 1 Explanation:
# The tree structure:
#       Chocolate Chip
#      /              \
# Peanut Butter     Oatmeal Raisin
#     /
#  Sugar

['Ginger Snap', 'Shortbread', 'Snickerdoodle']
# Example 2 Explanation:
# The tree structure:
#       Ginger Snap
#      /           \
# Shortbread   Snickerdoodle
