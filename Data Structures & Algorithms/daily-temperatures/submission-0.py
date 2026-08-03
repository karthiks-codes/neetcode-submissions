class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if temperatures[i] >= temperatures[j]:
                    count += 1
                    continue
                elif temperatures[i] < temperatures[j]:
                    count += 1
                    res[i] = count
                    break

        return res
            
                
                

        
        