# Given the root of a binary tree where each node represents a different plant species, return the value of the lowest common ancestor (LCA) of two given plants in the tree based on their species names. The species names are represented as strings, and the tree is structured according to lexicographical order (alphabetical order). The lowest common ancestor is defined between two species p and q as the lowest node in the tree that has both p and q as descendants (where we allow a node to be a descendant of itself).

# Assume all plants are a unique species. Note that each TreeNode has a reference to its parent node.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

# Note: the build_tree() function will not work for this problem because of the extra parent attribute. You must create your own tree manually for testing.

from collections import deque
class TreeNode():
    def __init__(self, species, parent=None, left=None, right=None):
        self.val = species
        self.parent = parent # Parent of node
        self.left = left
        self.right = right
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

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
def lca(root, p, q):
    lowest = None
    def helper(root, p, q):
        if not root:
            return False
        if p == root.val:
            return True
        if q == root.val:
            return True
        left = helper(root.left,p,q)
        right = helper(root.right,p,q)
        # print(root.val,left,right)
        if left and right:
            nonlocal lowest 
            lowest = root
        return left or right
    helper(root,p,q)
    return lowest.val if lowest else None


# Example Usage:

"""
          fern
        /      \
       /        \
  cactus        rose
   /  \         /   \
bamboo dahlia lily  oak
"""
fern = TreeNode("fern")
cactus = TreeNode("cactus", fern)
rose = TreeNode("rose", fern)
bamboo = TreeNode("bamboo", cactus)
dahlia = TreeNode("dahlia", cactus)
lily = TreeNode("lily", rose)
oak = TreeNode("oak", rose)

fern.left, fern.right = cactus, rose
cactus.left, cactus.right = bamboo, dahlia
rose.left, rose.right = lily, oak

print(lca(fern, "cactus", "rose"))
print(lca(fern, "bamboo", "oak"))
print(lca(fern, "bamboo", "dahlia"))
print(lca(fern, "lily", "oak"))

# Example Output:

# fern
# Example 1 Explanation: The lowest common ancestor of "cactus" and "rose" is "fern" because "fern" 
# is the lowest node in the tree that has both "cactus" and "rose" as descendants.

# fern
# Example 2 Explanation: The lowest common ancestor of "bamboo" and "oak" is "fern" because "fern" 
# is the lowest node in the tree that has both "bamboo" and "oak" as descendants.


#!/bin/python3

import math
import os
import random
import re
import sys
import ast
import json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Enter your code here. Read input from STDIN. Print output to STDOUT


