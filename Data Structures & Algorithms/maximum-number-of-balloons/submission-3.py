class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t = defaultdict(int)
        s = set("balloon")
        for i in text:
            if i in s:
                t[i] += 1
        m = min(t.values()) if len(t) > 0 else 0
        return min(m, t["l"]//2, t["o"]//2)

        

                

        
        