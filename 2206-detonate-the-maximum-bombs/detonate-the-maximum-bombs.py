class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        ans = 0

        for i in range(n):
            x1, y1, r1 = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                x2, y2, r2 = bombs[j]

                if (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) <= r1*r1:
                    graph[i].append(j)   


        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        for start in range(n):
            visited = set()
            dfs(start)
            ans = max(ans, len(visited))
        return ans

        