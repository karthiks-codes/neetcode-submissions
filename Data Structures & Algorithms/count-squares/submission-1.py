class CountSquares:

    def __init__(self):
        self.hmap = defaultdict(int)
        self.plist = []

    def add(self, point: List[int]) -> None:
        self.hmap[tuple(point)] += 1
        self.plist.append(point)

    def count(self, point: List[int]) -> int:
        result = 0
        qx, qy = point
        for x, y in self.plist:
            if (abs(qx - x) != abs(qy - y)) or qx == x or qy == y:
                continue

            result += self.hmap[(x, qy)] * self.hmap[(qx, y)]

        return result
        
