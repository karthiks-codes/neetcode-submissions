class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, i = stack.pop()
                res[i] = index - i
                
            stack.append((temp, index))

        return res
            
                
                

        
        