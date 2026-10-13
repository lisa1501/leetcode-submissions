class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        if not edges:
            return False

        visit = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node == destination:
                return True
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit and dfs(nei):
                    return True
            return False
                

        for key in graph:
            if key == source and key not in visit:
                if dfs(key):
                    return True
        return False
        
        