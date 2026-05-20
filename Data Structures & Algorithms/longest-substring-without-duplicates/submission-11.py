class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            seen = set()
        else:
            return 0
        if len(s)==1:
            return 1
        max1 = 0
        front = 0
        
        for i in range(0,len(s)):
            #.remove()
            #.discard()
            if s[i] in seen:
                while(s[i] in seen):
                    front+=1
                    seen.discard(s[front-1])
                    #if s[front]==s[i]:
                    #    break
                seen.add(s[i])
            else:
                seen.add(s[i])
            max1 = max(max1, i - front +1)


        
        
        return max1