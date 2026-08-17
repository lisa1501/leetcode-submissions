class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        res = 0

        def dfs(node):
            visited.add(node)
            for nei in range(n):
                if isConnected[node][nei] == 1 and nei not in visited:
                    dfs(nei)
                
        for node in range(n):
            if isConnected[node][node] == 1 and node not in visited:
                dfs(node)
                res += 1
        return res


        