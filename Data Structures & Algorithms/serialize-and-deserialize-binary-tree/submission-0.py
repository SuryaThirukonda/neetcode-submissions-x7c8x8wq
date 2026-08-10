# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root)->str:
        st = []
        def dfs(node):
            if node:
                st.append(f"{node.val}")
                dfs(node.left)
                dfs(node.right)
            else:
                st.append(f"n")
        dfs(root)
        return ",".join(st)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        data = data.split(",")
        it = iter(data)

        def dfs():
            tok = next(it)
            if tok == "n":
                return None

            node = TreeNode(int(tok))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
