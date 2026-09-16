class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res[even] = nums[i]
                even += 2
            else:
                res[odd] = nums[i]
                odd += 2

        return res
                
        