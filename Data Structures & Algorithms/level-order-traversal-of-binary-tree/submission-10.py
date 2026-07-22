# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        answer = []

        while queue:
            rowsize = len(queue)
            row = []

            for j in range(rowsize):
                curr = queue.popleft()
                if not curr:
                    continue
                row.append(curr.val)
                
                neighbors = [curr.left,curr.right]
                for i in neighbors:
                    queue.append(i)
            if (row):
                answer.append(row)
        return answer