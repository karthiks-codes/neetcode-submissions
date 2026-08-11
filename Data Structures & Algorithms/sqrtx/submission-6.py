class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        for i in range(1, x // 2 + 1):
            square = i * i
            if square == x:
                return i 
            elif square < x and (i + 1) ** 2 > x:
                return i
            
        