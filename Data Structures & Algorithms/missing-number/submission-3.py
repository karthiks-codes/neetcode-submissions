class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumn = (n * (n + 1))//2

        sumnums = sum(nums)

        return sumn - sumnums 

            
        