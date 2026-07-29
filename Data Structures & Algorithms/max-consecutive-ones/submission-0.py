class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curStreak = 0
        MaxStreak = 0
        i = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 1:
                curStreak += 1
            elif nums[i] == 0:
                curStreak = 0
            i += 1
            MaxStreak = max(curStreak, MaxStreak)

        return MaxStreak