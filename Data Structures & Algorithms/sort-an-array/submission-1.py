class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        res = []
        for _ in range(len(nums)):
            res.append(heapq.heappop(nums))

        return res
        