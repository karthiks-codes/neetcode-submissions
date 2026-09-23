class Solution:
    def rob(self, nums: List[int]) -> int:
        res1 = 0
        res2 = 0

        for i in range(len(nums)):
            m = max(res1 + nums[i], res2)
            res1 = res2
            res2 = m

        return res2

        