class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = defaultdict(int)
        for i in arr:
            c[i] += 1

        m = -1
        for key, value in c.items():
            if key == value:
                m = max(m, key)

        return m