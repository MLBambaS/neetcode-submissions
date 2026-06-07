class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for a,b in edges:
            if a==b: return False
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(i, prev):
            if i in visited: return False
            visited.add(i)
            for j in graph[i]:
                if j!=prev and not dfs(j,i): return False
            return True
        if not dfs(0, None): return False
        return len(visited) == n
        