class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0b11111111111111111111111111111111
        while b & mask:
            temp = (a & b) << 1
            a = (a ^ b) & mask
            b = temp & mask

        return a if a < (1 << 31) else ~(a ^ mask)

            
            
        