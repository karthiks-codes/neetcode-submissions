class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i, num in enumerate(nums):
            a.append([num,i])
        a.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            k = a[i][0] + a[j][0]
            if k == target:
                return [min(a[i][1], a[j][1]), max(a[i][1], a[j][1])]
            elif k < target:
                i += 1
            else:
                j -= 1
        return []



        
        