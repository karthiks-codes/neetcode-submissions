class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        nums = Counter(nums)
        for i in range(1, n):
            if nums[i] == 0:
                miss = i
            elif nums[i] == 2:
                duplicate = i

        return [duplicate, miss]
                
        