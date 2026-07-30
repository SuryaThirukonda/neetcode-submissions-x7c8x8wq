# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import PriorityQueue
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        bub = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            bub.append(node.val)
            traverse(node.right)

        traverse(root)
        return bub[k-1]