class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for i in nums:
            for j in ans.copy():
                ans += [ [i] + j]
        return ans


        