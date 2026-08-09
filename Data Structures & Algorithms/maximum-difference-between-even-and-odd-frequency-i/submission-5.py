class Solution:
    def maxDifference(self, s: str) -> int:
        s = Counter(s)

        maxOdd = 0
        minEven = 100

        for value in s.values():
            if value & 1:
                maxOdd = max(maxOdd, value)
            else:
                minEven = min(minEven, value)

        return maxOdd - minEven
        