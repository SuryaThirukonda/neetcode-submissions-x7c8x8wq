# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def dfs(node):
            nonlocal best

            if node is None:
                return 0          
            left = dfs(node.left)
            right = dfs(node.right)

            left  = max(0,left)
            right = max(0,right)

            best = max(best, left+node.val+right)           
            return node.val + max(left,right)

        dfs(root)
        return best
