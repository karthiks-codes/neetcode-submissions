class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = math.prod(nums)

        def signum(prod):
            if prod == 0:
                return 0 
        
            return abs(prod) // prod

        return signum(prod)
