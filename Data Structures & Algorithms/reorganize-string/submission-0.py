class Solution:
    def reorganizeString(self, s: str) -> str:
        if s == "":
            return ""
        count = defaultdict(int)
        for i in s:
            count[i] += 1

        heapp = [[value, key] for key, value in count.items()]
        heapq.heapify_max(heapp)

        res = ""
        previous = None
        while heapp or previous:
            if previous and not heapp:
                return ""
            
            value, key = heapq.heappop_max(heapp)
            res += key
            value -= 1

            if previous:
                heapq.heappush_max(heapp, previous)
                previous = None

            if value != 0:
                previous = [value ,key]
        return res
            

        

