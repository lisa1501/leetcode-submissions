class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Topological Sort for rowConditions, colConditions, similar to Course Schedule II
        # if Topological Sort for rowConditions is not empty list, loop thru list, enumerate, map num -> idx(row), return []
        # if Topological Sort for colConditions is not empty list, loop thru list, enumerate, map num -> idx(col), resutn []
        # build matrix,with k zero, update matrix[r][c] to num, map num -> idx(row), map num -> idx(col),
        # Time:  O(k*k + R + C) Space: O(k + R + C), R:num of rowConditions, C:num of colConditions
        def topo_sort(conditions):

            graph = defaultdict(list)
            indegree = [0] * (k + 1)

            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1

            q = deque()

            for node in range(1, k + 1):
                if indegree[node] == 0:
                    q.append(node)

            order = []

            while q:

                node = q.popleft()
                order.append(node)

                for nei in graph[node]:

                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        q.append(nei)

            # Cycle
            if len(order) != k:
                return []
            return order

        # topological sort rows, cols
        row_order = topo_sort(rowConditions) #O(R)
        col_order = topo_sort(colConditions) #O(C)

        # early return 
        if not row_order:
            return []
        if not col_order:
            return []

        # map number -> row
        row_pos = {}
        for r, num in enumerate(row_order):
            row_pos[num] = r
        # map number -> column
        col_pos = {}
        for c, num in enumerate(col_order):
            col_pos[num] = c

        # build matrix
        matrix = [[0] * k for _ in range(k)] #O(k*k)
        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            matrix[r][c] = num

        return matrix
        