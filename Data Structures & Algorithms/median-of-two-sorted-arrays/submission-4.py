class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                ans.append(nums2[j])
                j += 1
            else:
                ans.append(nums1[i])
                ans.append(nums2[j])
                i, j = i + 1, j + 1
        while i < n1:
            ans.append(nums1[i])
            i += 1
        while j < n2:
            ans.append(nums2[j])
            j += 1
        
        if (n1 + n2) % 2:
            return ans[(n1 + n2)//2]
        else:
            return (ans[(n1+n2)//2 - 1] + ans[(n1+n2)//2])/2
        