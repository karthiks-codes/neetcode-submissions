class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list)

        for parent, child in edges:
            adjList[parent].append(child)
            adjList[child].append(parent)

        def dfs(current, parent):
            time = 0

            for child in adjList[current]:
                if child == parent:
                    continue

                cTime = dfs(child, current)
                
                if hasApple[child] or cTime > 0:
                    time += 2 + cTime

            return time

        return dfs(0, -1) 



        