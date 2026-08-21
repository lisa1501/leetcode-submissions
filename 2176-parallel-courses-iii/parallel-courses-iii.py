class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1) #there are n courses labeled from 1 to n. so n+1

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque()
        finish = [0] * (n + 1)

        # Courses without prerequisites
        for course in range(1, n + 1):#labeled from 1 to n. 
            if indegree[course] == 0:
                queue.append(course)
                # array time where time[i] denotes how many months it takes to complete the (i+1)th course
                # so array time where time[i - 1] denotes how many months it takes to complete the i th course
                finish[course] = time[course - 1]

        while queue:

            course = queue.popleft()

            for nxt in graph[course]:

                finish[nxt] = max(
                    finish[nxt],
                    finish[course] + time[nxt - 1]
                )

                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    queue.append(nxt)

        return max(finish)