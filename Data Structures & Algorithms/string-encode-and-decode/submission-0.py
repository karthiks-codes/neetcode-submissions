class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        if len(strs) == 0:
            return res
        for i in strs:
            res = res + str(len(i))
            res = res + '#'
            res = res + i

        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)
        while i < n:
            j = i

            while s[j] != '#':
                j += 1
                
            l = int(s[i:j])
            i = j + 1
            j = i + l

            result.append(s[i:j])
            i = j
        
        return result

        
