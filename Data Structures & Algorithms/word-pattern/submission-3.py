class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = defaultdict(str)
        e = defaultdict(str)
        s = s.split()
        
        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if d[pattern[i]] and d[pattern[i]] != s[i]:
                return False
            if e[s[i]] and e[s[i]] != pattern[i]:
                return False

            d[pattern[i]] = s[i]
            e[s[i]] = pattern[i]

        return True

        