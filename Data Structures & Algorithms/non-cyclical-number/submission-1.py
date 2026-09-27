class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            digits = str(n)
            square = 0
            for i in digits:
                square += int(i) * int(i)

            if square == 1:
                return True
            
            if square in seen:
                return False

            seen.add(square)
            n = square





        


        