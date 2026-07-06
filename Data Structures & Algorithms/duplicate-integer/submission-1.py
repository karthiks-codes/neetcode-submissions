class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set()
        for i in nums:
            num.add(i)
        if len(num) < len(nums):
            return True
        return False

        