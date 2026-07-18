# What is time and space complexity of the following

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.value = val
        self.left_child = left
        self.right_child = right

def sum_tree_levels(node):
    def helper(n, depth, level_sums):
        if not n:
            return
        if depth == len(level_sums):
            level_sums.append(0)
        level_sums[depth] += n.value
        helper(n.left_child,depth+1,level_sums)
        helper(n.right_child,depth+1,level_sums)

    level_sums = []
    helper(node,0,level_sums)
    return level_sums

# what is the output of snippet:
def mystery_function(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.value*2)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print("stuck")
    return result

#Test cases
root = TreeNode(1)
root.left_child = TreeNode(2)
root.right_child = TreeNode(3)
root.left_child.left_child = TreeNode(4)
root.left_child.right_child = TreeNode(5)
root.right_child.left_child = TreeNode(6)
root.right_child.right_child = TreeNode(7)

print(mystery_function(root))