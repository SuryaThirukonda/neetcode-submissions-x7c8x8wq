class Solution:
    def countBits(self, n: int) -> List[int]:
        lt = []
        for i in range(n+1):
            lt.append(i)
            count = 0
            while lt[i]:
                count+= lt[i]%2
                lt[i] = lt[i]>>1
            lt[i]=count
        return lt
        