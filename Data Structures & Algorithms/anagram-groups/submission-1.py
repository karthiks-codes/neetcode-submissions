class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            so = ''.join(sorted(i))
            res[so].append(i)
        return list(res.values())
        

        
        