class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_to_course = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre_course in prerequisites:
            pre_to_course[pre_course].append(course)
            indegree[course] += 1
            
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []

        while q:
            pre_crs = q.popleft()
            order.append(pre_crs)

            for nxt_crs in pre_to_course[pre_crs]:
                indegree[nxt_crs] -= 1

                if indegree[nxt_crs] == 0:
                    q.append(nxt_crs)

        if len(order) == numCourses:
            return order
        return []
        