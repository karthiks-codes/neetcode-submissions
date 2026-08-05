class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        charCount = Counter(chars)
        for i in words:
            count = Counter(i)
            Flag = True
            for j in count:
                if charCount[j] < count[j]:
                    Flag = False
                    break

            if Flag:
                sum += len(i)

        return sum