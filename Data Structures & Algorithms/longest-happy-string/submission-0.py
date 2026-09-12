class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        m = [
            [a, "a"],
            [b, "b"],
            [c, "c"]
        ]
        charMap = []
        for val, key in m:
            if val != 0:
                heapq.heappush_max(charMap, [val, key])

        res = ""
        

        while charMap:
            value, key = heapq.heappop_max(charMap)
            if len(res) > 1 and res[-1] == res[-2] == key:
                if not charMap:
                    break
                v, k = heapq.heappop_max(charMap)
                res += k
                v -= 1
                if v:
                    heapq.heappush_max(charMap, [v, k])
                heapq.heappush_max(charMap, [value, key])

            else:
                res += key
                value -= 1
                
                if value:
                    heapq.heappush_max(charMap, [value, key])

            
        return res        
        