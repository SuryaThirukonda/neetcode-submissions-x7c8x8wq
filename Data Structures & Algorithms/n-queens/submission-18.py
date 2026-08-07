class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        #initialize board to 0 first
        board = [["." for i in range(n)] for j in range(n)]
        results = []

        def checkValid( board, q):
            x = q[0]
            y = q[1]
            t1 = x
            t2 = y
            for i in range(y):
                if board[x][i] =="Q":
                    return False

            #check diagonal
            while (t1 >0 and t2>0):
                t1-=1
                t2-=1
                if board[t1][t2] == "Q":
                    return False
            while x<len(board)-1 and y>0:
                x+=1
                y-=1
                if board[x][y] =="Q":
                    return False
            return True
        
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
                if (checkValid(board,temp)):
                    board[i][col] = "Q"
                    findAns(board,col+1)
                    board[i][col]="."

        
        
        
        findAns(board,0)
        return results
    
