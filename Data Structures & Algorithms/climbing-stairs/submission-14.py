class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n

        dp = [0,1,2]
        for i in range(3,n+1):
            dp.append(dp[i-1]+dp[i-2])

        return dp[n]
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