class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        res = []
        for i in nums2:
            if i in nums1:
                res.append(i)  
                nums1.remove(i)

        return res
