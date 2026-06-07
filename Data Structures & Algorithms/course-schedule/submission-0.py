class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        def dfs(i, visited):
            if i in visited:
                return False
            if graph[i] == []:
                return True
            visited.add(i)
            for j in graph[i]:
                if not dfs(j,visited):
                    return False
            visited.remove(i)
            return True
        for c in range(numCourses):
            if not dfs(c,set()):
                return False
        return True
        