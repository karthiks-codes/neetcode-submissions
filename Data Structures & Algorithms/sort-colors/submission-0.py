class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        pointer = 0
        for i in range(3):
            while count[i]:
                nums[pointer] = i
                count[i] -= 1
                pointer += 1

        



        