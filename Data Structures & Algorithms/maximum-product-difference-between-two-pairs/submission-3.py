class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        m1 = m2 = 0
        n1 = n2 = 10001

        for num in nums:
            if num > m1:
                m1, m2 = num, m1
            elif num > m2:
                m2 = num

            if num < n1:
                n1, n2 = num, n1
            elif num < n2:
                n2 = num


        return m1 * m2 - n1 * n2
            

        

        

        