class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        i = 1
        while i <= (num) // 2: 
            s = i ** 2
            if s == num:
                return True
            elif s > num:
                return False

            i -= 1

        



        