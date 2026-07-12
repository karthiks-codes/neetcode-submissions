from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        s1Count = Counter(s1)

        left = 0
        for i in range(k,len(s2)+1):
            if s1Count == Counter(s2[left:i]):
                return True
            left += 1
    
        return False


            
            
        



        