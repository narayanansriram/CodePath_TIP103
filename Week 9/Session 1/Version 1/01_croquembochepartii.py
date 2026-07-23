# You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

# Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, traverse the croquembouche in tier order (i.e., level by level, left to right).

# You should return a list of lists where each inner list represents a tier (level) of the croquembouche and the elements of each inner list contain the flavors of each cream puff on that tier (node vals from left to right).

# Note: The build_tree() and print_tree() functions both use variations of a level order traversal. To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

# Hint: Level order traversal, BFS

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

from collections import deque
def listify_design(design):
    q = deque()
    q.append(design)
    result = []
    while q:
        lev = []
        for _ in range(len(q)):
            root = q.popleft()
            lev.append(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        result.append(lev)
    return result

# Example Usage:

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(listify_design(croquembouche))

# Example Output:

# [['Vanilla'], ['Chocolate', 'Strawberry'], ['Vanilla', 'Matcha']]
