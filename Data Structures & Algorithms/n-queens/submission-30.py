class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        #initialize board to 0 first
        board = [["."]*n for j in range(n)]
        results = []
        row = set()
        pos = set()
        neg = set()
        
        def findAns( board,col):
            if (col==len(board)):
                temp =["" for i in range(len(board))]
                for i in range(len(board)):
                    temp[i]="".join(board[i])

                results.append(temp)
                return

            for i in range(len(board)):
                temp = [i,col]

                #if its valid, then stard a new tree path
                if not (i in row or i-col in pos or i+col in neg):
                    board[i][col] = "Q"
                    row.add(i)
                    pos.add(i-col)
                    neg.add(i+col)

                    findAns(board,col+1)
                    
                    #reset for next iteration
                    board[i][col]="."
                    row.remove(i)
                    pos.remove(i-col)
                    neg.remove(i+col)

        
        
        
        findAns(board,0)
        return results
    
