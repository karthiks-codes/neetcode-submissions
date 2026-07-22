class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        n = bin(n)[2:]

        if n.count('1') == 1:
            return True
        return False


        