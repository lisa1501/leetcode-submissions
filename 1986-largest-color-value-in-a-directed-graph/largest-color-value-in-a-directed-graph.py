class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        # Step 1: Build graph
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Step 2: dp[node][c] = maximum count of color c
        # on any path ending at node
        dp = [[0] * 26 for _ in range(n)]

        for node in range(n):
            color_idx = ord(colors[node]) - ord('a')
            dp[node][color_idx] = 1

        # Step 3: Start with all nodes having indegree 0
        queue = deque(
            node for node in range(n)
            if indegree[node] == 0
        )

        processed = 0
        ans = 0

        # Step 4: Topological BFS + DP transitions
        while queue:
            node = queue.popleft()
            processed += 1

            # Best color count among paths ending at this node
            ans = max(ans, max(dp[node]))

            for nei in graph[node]:
                for c in range(26):
                    color_bonus = (
                        1 if c == ord(colors[nei]) - ord('a') else 0
                    )

                    dp[nei][c] = max(
                        dp[nei][c],
                        dp[node][c] + color_bonus
                    )

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        # If some nodes were not processed, the graph has a cycle
        if processed != n:
            return -1

        return ans