class TimeMap:

    def __init__(self):
        self.kv = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
        self.kv[key].append([value, timestamp])
            
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        value = self.kv.get(key, [])
        l = 0
        r = len(value) - 1
        while l <= r:
            mid = r + (l - r) // 2
            if value[mid][1] <= timestamp:
                result = value[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result
        
        
