class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmax = 1
        cmin = 1
        for i in nums:
            temp = cmax
            cmax = max(temp * i, cmin * i, i)
            cmin = min(temp * i, cmin * i, i)
            res = max(res, cmax)
        return res
        