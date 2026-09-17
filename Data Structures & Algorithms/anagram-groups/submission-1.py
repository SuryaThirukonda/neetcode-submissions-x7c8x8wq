class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}

        for st in strs:
            temp = "".join(sorted(st))
            if temp in dicts:
                dicts[temp].append(st)
            else:
                dicts[temp] = [st]

        ans = []
        for key in dicts:
            ans.append(dicts[key])
        
        return ans

                
