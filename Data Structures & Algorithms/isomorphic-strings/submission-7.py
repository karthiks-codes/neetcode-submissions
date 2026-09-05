class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapped = {}
        used = set()

        for i in range(len(s)):
            if s[i] in mapped:
                if mapped[s[i]] != t[i]:
                    return False

            else:
                if t[i] in used:
                    return False

                mapped[s[i]] = t[i]
                used.add(t[i])

        return True