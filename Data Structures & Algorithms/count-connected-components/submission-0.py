class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(i,prev):
            if i in visited: return
            visited.add(i)
            for j in graph[i]:
                if j!=prev: 
                    dfs(j,i)
        count = 0
        while len(visited)<n:
            for i in range(n):
                if i not in visited:
                    count+=1
                    dfs(i, None)
        return count
        