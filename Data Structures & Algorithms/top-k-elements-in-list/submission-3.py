class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        co = Counter(nums)
        li = []
        for key,value in co.most_common(k):
            li.append(key)

        return li

        
        
        
    