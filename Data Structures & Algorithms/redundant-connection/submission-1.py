class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = {i:i for i in range(1,n+1)}
        rank = {i:0 for i in range(1,n+1)}
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x,y):
            p1 = find(x)
            p2 = find(y)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                par[p1] = p2
            elif rank[p2] < rank[p1]:
                par[p2] = p1
            else:
                par[p1] = p2
                rank[p2]+=1
            return True
        for a,b in edges:
            if not union(a,b): return [a,b]
        