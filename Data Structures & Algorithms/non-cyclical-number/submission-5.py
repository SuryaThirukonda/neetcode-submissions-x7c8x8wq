class Solution:
    def isHappy(self, n: int) -> bool:
        map = {}
    
        while (n!=1 and n not in map):
            map[n]=1
            t = str(n)
            n=0
            for char in t:
                n+=(int(char))**2
            

        if (n==1):
            return True
        else:
            return False