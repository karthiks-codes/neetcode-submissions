class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ind = [i for i in range(len(names))]
        ind.sort(key = lambda x: heights[x], reverse = True)
        res = []
        for i in ind:
            res.append(names[i])
        return res
        