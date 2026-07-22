class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        lis = defaultdict(int)

        for i in nums:
            lis[i] = lis[i] ^ i
        

        for value in lis.values():
            if value != 0:
                print(value)
                return False
        
        return True
       

        


        