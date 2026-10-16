class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(start):

            dist = [float("inf")] * n
            dist[start] = 0

            heap = [(0, start)]

            while heap:

                curr_dist, node = heapq.heappop(heap)

                if curr_dist > dist[node]:
                    continue

                for nei, weight in graph[node]:

                    new_dist = curr_dist + weight

                    if new_dist < dist[nei]:

                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))

            return dist

        answer = None
        smallest = float("inf")

        for city in range(n):

            dist = dijkstra(city)

            reachable = sum(d <= distanceThreshold for d in dist) - 1   # exclude itself

            if reachable <= smallest:
                smallest = reachable
                answer = city

        return answer
        