import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)

        for _ in range(k):
            maxNumber = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, math.floor(math.sqrt(maxNumber)))

        return sum(gifts)



        

        