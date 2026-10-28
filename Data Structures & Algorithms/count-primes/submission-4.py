class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0

        #True means it is a prime, false is no, 0 and 1 are not primes
        arr = [True] *(n)
        arr[0] = False
        arr[1] = False

        curr  = 2

        while curr *curr <n:
            for i in range(curr*curr, n, curr):
                arr[i] = False

            #step curr forward once
            curr+=1

            #check if the next curr is alr checked
            if arr[curr] == False:
                curr+=1
        
        count=0

        for c in arr:
            if c:
                count+=1

        return count
