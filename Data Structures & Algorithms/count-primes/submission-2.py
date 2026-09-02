class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        Count = 0
        arr = [False] * n

        for i in range(2, n):
            if not arr[i]:
                Count += 1
                for j in range(i * i, n, i):
                    arr[j] = True
        return Count


        