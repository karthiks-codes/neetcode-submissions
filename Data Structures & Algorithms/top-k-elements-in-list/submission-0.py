from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        co = Counter(nums)
        li = []
        for i,j in co.most_common(k):
            li.append(i)
        return li

        