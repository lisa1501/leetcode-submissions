class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        inf = float('inf')
        # dist[i][j] = convert character i -> character j minimum cost
        dist = [[inf] * 26 for _ in range(26)]
        # convert same chars cost 0
        for i in range(26):
            dist[i][i] = 0

        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            # There may be multiple conversions between the same two characters
            dist[u][v] = min(dist[u][v], cost[i])
           
        # Floyd-Warshall
        # a → b = 10, a → c = 2, c → b = 3 , dist[a][b] = 10,  k = c, a → c → b, dist[a][c] + dist[c][b]= 2 + 3 = 5
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

        ans = 0
        for i in range(len(source)):
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')

            if dist[u][v] == inf:
                return -1

            ans += dist[u][v]

        return ans


        
        