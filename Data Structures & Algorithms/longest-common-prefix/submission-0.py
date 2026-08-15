class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = ""
        for j in range(len(strs[0])):
            c = ""
            for i in range(len(strs)):
                if j < len(strs[i]):
                    if not c:
                        c = strs[i][j]
                    elif strs[i][j]!=c:
                        return final
                    else:
                        continue
                else:
                    return final
            final+=c

        return final