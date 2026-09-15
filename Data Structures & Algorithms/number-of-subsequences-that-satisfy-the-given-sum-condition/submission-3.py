class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        r = len(nums) - 1
        count = 0
        mod = (10 ** 9) + 7

        for i in range(n):
            l = nums[i]
            if nums[i] > target:
                break

            while (l + nums[r]) > target and i <= r:
                r -= 1

            if i <= r:
                count += 2 ** (r - i)

            r = len(nums) - 1

        return count % mod

        



        