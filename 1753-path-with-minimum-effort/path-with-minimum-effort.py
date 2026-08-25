class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra's Algorithm, time:O(rows*cols*log(rows*cols)), space:O(rows*cols)
        ROWS = len(heights)
        COLS = len(heights[0])

        effort = [[float("inf")] * COLS for _ in range(ROWS)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]  # (effort, row, col)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            curr_effort, r, c = heapq.heappop(heap)

            if (r, c) == (ROWS - 1, COLS - 1):
                return curr_effort

            if curr_effort > effort[r][c]:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    # A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
                    weight = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(curr_effort, weight)

                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return 0
        