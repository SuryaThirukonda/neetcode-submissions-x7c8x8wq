class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in map1:
                map1[i]+=1
            else:
                map1[i]=1
        for i in t:
            if i in map1:
                if map1[i] ==0:
                    return False
                map1[i]-=1
            else:
                return False

        return True

            
        