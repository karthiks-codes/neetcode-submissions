class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        count = 0
        for value in counter.values():
            count += (value * (value - 1)) // 2
        return count

        