class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        k = 0

        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1

            chars[k] = chars[i]
            k += 1
            if j - i > 1:
                count = j - i
                for di in str(count):
                    chars[k] = di
                    k += 1

            i = j

        
        return k