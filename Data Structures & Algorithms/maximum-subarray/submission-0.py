class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]

        cur = 0

        for num in nums:
            cur = max(cur, 0)
            cur = cur + num
            maxx = max(cur, maxx)

        return maxx



        
        