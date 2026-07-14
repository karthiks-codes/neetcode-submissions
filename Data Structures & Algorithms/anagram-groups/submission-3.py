class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            o = ''.join(sorted(i))
            res[o].append(i)
        
        return list(res.values())
        

        
        