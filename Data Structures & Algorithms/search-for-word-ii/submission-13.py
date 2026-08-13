class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        res = []
        for word in words:
            curr = trie
            for c in word:
                curr = curr.setdefault(c,{})
            curr['!'] = word
        
        def dfs(i,j,curr):
            
            if '!' in curr:
                res.append(curr['!'])
                del curr['!']
            
            if i>=len(board) or i<0 or j<0 or j>=len(board[0]):
                return 

            temp = board[i][j]
            board[i][j] = '+'

            #launch dfs in each direction, traverse into trie deeper to check if word exists
            if i<len(board)-1 and board[i+1][j] in curr:
                dfs(i+1,j,curr[board[i+1][j]])
            if j<len(board[0])-1 and board[i][j+1] in curr:
                dfs(i,j+1,curr[board[i][j+1]])
            if i>0 and board[i-1][j] in curr:
                dfs(i-1,j,curr[board[i-1][j]]) 
            if j>0 and board[i][j-1] in curr:
                dfs(i,j-1,curr[board[i][j-1]])
            
            board[i][j]=temp
            
            return
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(i,j,trie[board[i][j]])

        return res

