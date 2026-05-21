class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s)==0:
            return 0
        
        max1 = 0
        start = 0
        curr=s[0]
        freq = {}
        
        for i in range(len(s)):
            
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
            if (freq[s[i]]>freq[curr]):
                curr = s[i]
            # add the frequencies of the next character
            if ((i-start+1)-freq[curr] >k):
                freq[s[start]]-=1
                if (freq[s[start]]>freq[curr]):
                    curr = s[start]
                start+=1
            max1 = max(max1, i-start +1)
                
        return max1
            
