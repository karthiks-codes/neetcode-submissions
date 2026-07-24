class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ans = nums.copy()

        m_heap = [[value, index] for index, value in enumerate(nums)]
        heapq.heapify(m_heap)

        for _ in range(k):
            v, i = heapq.heappop(m_heap)
            ans[i] = v * multiplier
            heapq.heappush(m_heap, [ans[i], i])

        return ans

            

        