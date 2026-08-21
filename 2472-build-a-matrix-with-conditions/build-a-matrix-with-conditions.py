class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def top_sort(conditions):
            graph = defaultdict(list)
            indegree = [0] * (k+1)

            for pre, nxt in conditions:
                graph[pre].append(nxt)
                indegree[nxt] += 1
            
            q = deque([])

            for i in range(1,k+1):
                if indegree[i] == 0:
                    q.append(i)

            order = []

            while q:
                for _ in range(len(q)):
                    pre = q.popleft()
                    order.append(pre)

                    for nxt in graph[pre]:
                        indegree[nxt] -= 1

                        if indegree[nxt] == 0:
                            q.append(nxt)

            if len(order) != k:
                return []
            return order

        top_sort_rowConditions = top_sort(rowConditions)
        top_sort_colConditions= top_sort(colConditions)

        if not top_sort_rowConditions:
            return []

        if not top_sort_colConditions:
            return []

        row_pos ={}
        for r, num in enumerate(top_sort_rowConditions):
            row_pos[num] = r

        col_pos ={}
        for c, num in enumerate(top_sort_colConditions):
            col_pos[num] = c

    
        matrix = [[0] * k for _ in range(k)] 
        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            matrix[r][c] = num

        return matrix


        