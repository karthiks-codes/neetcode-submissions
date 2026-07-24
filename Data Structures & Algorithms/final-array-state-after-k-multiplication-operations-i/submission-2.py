class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = []
        for i, j in enumerate(nums):
            arr.append([j, i])

        heapq.heapify(arr)
        
        for _ in range(k):
            x = heapq.heappop(arr)
            heapq.heappush(arr, [x[0] * multiplier,x[1]])
        

        arr.sort(key = lambda x: x[1])

        ans = [0] * len(nums)
        while arr:
            value, index = arr.pop(0)
            ans[index] = value
        
        return ans

            

        