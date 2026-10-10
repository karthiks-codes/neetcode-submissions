class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                tsum = num + nums[left] + nums[right]
                if tsum == 0:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif tsum > 0:
                    right -= 1
                else:
                    left += 1

        return triplets

            





            


        