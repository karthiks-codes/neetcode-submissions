class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hmap = {}
        for i, h in enumerate(heights):
            print(i, h)
            hmap[h] = i

        heights.sort(reverse = True)
        res = []
        for i in heights:
            index = hmap[i]
            res.append(names[index])

        return res



        