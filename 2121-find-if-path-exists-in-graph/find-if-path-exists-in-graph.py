class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        visit = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visit):
            if node == destination:
                return True
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit and dfs(nei, visit):
                    return True
            return False
                
        return dfs(source, visit)