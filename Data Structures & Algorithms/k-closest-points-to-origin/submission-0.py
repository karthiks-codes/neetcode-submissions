class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in points:
            heapq.heappush(heap, [(i[0] ** 2 + i[1] ** 2), [i[0], i[1]]])
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


    

