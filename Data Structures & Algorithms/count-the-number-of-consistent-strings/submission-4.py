class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = len(words)
        for i in words:
            for j in i:
                if j not in allowed:
                    count -= 1
                    print(j)
                    break
        return count
        


        