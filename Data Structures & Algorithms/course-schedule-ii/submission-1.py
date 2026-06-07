class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)
        visiting, visited = set(), set()
        def dfs(i):
            if i in visiting: return False
            if i in visited: return True
            visiting.add(i)
            for j in graph[i]:
                if not dfs(j): return False
            visiting.remove(i)
            visited.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i): return []
        return res
        

        