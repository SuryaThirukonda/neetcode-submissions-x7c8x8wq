class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""

        string = ""

        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if len(strs[i])==0:
                    return ""
                if j>= len(strs[i]):
                    return string
                if (strs[i][j]!= strs[0][j]):
                    return string
            string += strs[0][j]
            if j != len(strs[0])-1:
                curr = strs[0][j+1]
        

        return string

            
        
        
        