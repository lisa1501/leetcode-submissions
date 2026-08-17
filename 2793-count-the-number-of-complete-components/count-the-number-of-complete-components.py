class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visited.add(node)
            nodes = 1
            edges = len(graph[node])
            for nei in graph[node]:
                if nei not in visited:
                    nei_nodes, nei_edges = dfs(nei)
                    nodes += nei_nodes
                    edges += nei_edges

            return (nodes, edges)
                
        for node in range(n):
            if node not in visited:
                nodes, edges =dfs(node)
                
                if edges == (nodes-1) * nodes:
                    res += 1
                
        return res