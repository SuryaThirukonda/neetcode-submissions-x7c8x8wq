class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1

        for i in range(1,n):
            temp = two
            two = one + two
            one = temp
        return two

        '''
        one,two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
        '''
            
        '''
        cache = [-1 for i in range(n)]

        def dfs(i):
            if i==n:
                return 1
            elif i>n:
                return 0
            elif cache[i]!= -1:
                return cache[i]

            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)

        '''