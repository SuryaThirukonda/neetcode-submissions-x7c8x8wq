# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        m = {}
        for i in range(len(inorder)):
            m[inorder[i]]=i

        #index of split in inorder, and the length of preorder after 1

        def build(preind, ind1,ind2):
            if ind1>ind2:
                return None

            root = TreeNode(preorder[preind])
            index = m[root.val]
            
            size = index-ind1
            root.left = build(preind+1,ind1,index-1)
            root.right = build(preind+size+1,index+1,ind2)

            return root

        
        return build(0,0,len(inorder)-1)