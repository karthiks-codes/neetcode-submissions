class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            ele = nums2.index(nums1[i])
            nextGreater = -1
            
            for j in range(ele + 1, len(nums2)):
                print(nums2[j])
                if nums2[j] > nums2[ele]:
                    nextGreater = nums2[j]
                    break
            res.append(nextGreater)

        return res

        