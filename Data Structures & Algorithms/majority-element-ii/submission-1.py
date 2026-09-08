class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = Counter(nums)
        res = []
        for key, value in n.items():
            if value > len(nums)//3:
                res.append(key)

        return res

        