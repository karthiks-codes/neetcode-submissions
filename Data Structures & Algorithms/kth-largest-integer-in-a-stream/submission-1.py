class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify_max(nums)
        

    def add(self, val: int) -> int:
        heapq.heappush_max(self.nums,val)
        temp = []
        for _ in range(self.k):
            popped = heapq.heappop_max(self.nums)
            temp.append(popped)

        for i in temp:
            heapq.heappush_max(self.nums, i)
        return popped



        
        
