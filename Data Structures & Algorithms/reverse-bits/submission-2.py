class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n.rjust(32,'0')
        
        n = n[::-1]

        n = int(n, 2)

        return n