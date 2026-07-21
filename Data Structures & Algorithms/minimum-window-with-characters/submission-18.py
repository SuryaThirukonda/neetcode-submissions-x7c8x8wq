class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        have = {}
        
        for ch in t:
            if ch in need:
                need[ch]+=1
            else:
                need[ch]=1
            have[ch]=0

        n = len(need)
        h = 0

        first = 0
        last = 0

        best = (0,0)
        length = 1001
        for last in range(len(s)):
            curr = s[last]

            if curr in have:
                have[curr]+=1
                
                if (have[curr]==need[curr]):
                    h+=1
                
            while (h==n):
                #save the current window
                if (last-first+1)<length:
                    best = (first,last)
                    length = last-first+1
                left = s[first]
                if left in have:
                    have[left]-=1
                    if (have[left]<need[left]):
                        h-=1
                #move first pointer forward, until have is decremented
                first+=1

        if (length == 1001):
            return ""
        return s[best[0]:best[1]+1]
                