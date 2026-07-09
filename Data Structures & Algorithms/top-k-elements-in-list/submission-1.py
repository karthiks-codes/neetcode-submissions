from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        re = []
        for i, j in count.most_common(k):
            re.append(i)
        return re

        

        