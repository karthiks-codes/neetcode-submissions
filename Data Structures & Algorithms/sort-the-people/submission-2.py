class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hmap = zip(names, heights)
        hmap = sorted(hmap, key = lambda x: x[1], reverse = True)
        res = []
        for name, height in hmap:
            res.append(name)

        return res

        



        