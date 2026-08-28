class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = set()
        trustMap = defaultdict(set)
        
        for i in trust:
            people.add(i[0])
            people.add(i[1])
            trustMap[i[0]].add(i[1])

        n = len(people)
        print(people)
        print(trustMap)
        print(trustMap.keys())
        for i in people:
            flag = True
            if i not in trustMap.keys():
                for j in trustMap.values():
                    if i not in j:
                        flag = False
                if flag: 
                    return i
        return -1

        