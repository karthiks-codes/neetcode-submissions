class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] = count[i] + 1
        res = []
        for key, value in islice(sorted(count.items(),key = lambda x: x[1],reverse = True ),k):
            res.append(key)
        return res
