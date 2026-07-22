class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = set()

        for num in nums:
            if num not in n:
                n.add(num)
            else:
                n.remove(num)

        if n:
            return False
        return True
        
       

        


        