class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])

        for i in words:
            cur = Counter(i)
            for j in c:
                c[j] = min(c[j], cur[j])
        
        res = []
        for i in c:
            for j in range(c[i]):
                res.append(i)

        return res
