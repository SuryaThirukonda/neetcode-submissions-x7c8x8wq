class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def crawl(r,c,word):
            #base case
            if len(word)==0:
                return True

            #bounds check for recursion
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) :
                return

            if (board[r][c]==word[0]):
                temp = word[:1]
                board[r][c]="+"

                #crawl all directions
                c1 = crawl(r+1,c,word[1:])
                c2 = crawl(r,c+1,word[1:])
                c3 = crawl(r-1,c,word[1:])
                c4 = crawl(r,c-1,word[1:])

                board[r][c]=temp
                if c1 or c2 or c3 or c4:
                    return True
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    cond = crawl(r,c,word)
                    if cond:
                        return True
        return False            