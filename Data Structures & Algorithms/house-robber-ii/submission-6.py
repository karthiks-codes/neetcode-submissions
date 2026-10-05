class Solution:
    def robber(self, nums: List[int]) -> int:
        res1 = 0
        res2 = 0

        for i in nums:
            m = max(res1 + i, res2)
            res1 = res2
            res2 = m                             

        return res2
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robber(nums[: -1]), self.robber(nums[1:]))