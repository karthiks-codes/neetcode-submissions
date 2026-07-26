class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        sum = 0
        for i in count:
            if count[i] == 1:
                return -1

            sum += math.ceil(count[i] / 3)

        return sum
        