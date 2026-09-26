class Solution:
    def countOdds(self, low: int, high: int) -> int:
        rLen = high - low + 1
        count = rLen // 2
        if low & 1 and rLen & 1:
            count += 1
        return count
        