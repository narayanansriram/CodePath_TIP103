from collections import deque
def delete_node(root, key):
    # Write your code here
    if not root:
        return
    if key<root.val:
        root.left = delete_node(root.left,key)
    elif key > root.val:
        root.right = delete_node(root.right,key)
    else:
        if not root.left and not root.right:
            return None
        else:
            succ = root.right
            if succ:
                while succ.left:
                    succ = succ.left
                root.val = succ.val
                root.right = delete_node(root.right,succ.val)
            else:
                succ = root.left
                while succ.right:
                    succ = succ.right
                root.val = succ.val
                root.left = delete_node(root.left, succ.val)
    
    return root

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
        if node.left_child:
            queue.append(node.left_child)
        if node.right_child:
            queue.append(node.right_child)
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