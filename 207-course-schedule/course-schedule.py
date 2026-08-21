class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_to_course = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre_course in prerequisites:
            pre_to_course[pre_course].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            for _ in range(len(q)):
                pre_crs = q.popleft()
                completed += 1

                for nxt_crs in pre_to_course[pre_crs]:
                    indegree[nxt_crs] -= 1

                    if indegree[nxt_crs] == 0:
                        q.append(nxt_crs)

        return completed == numCourses

# Parallel Courses — LC 1136
        # pre_to_course = defaultdict(list)
        # indegree = [0] * numCourses

        # for course, pre_course in prerequisites:
        #     pre_to_course[pre_course].append(course)
        #     indegree[course] += 1
            
        # q = deque()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)

        # completed = 0
        # smesters = 0

        # while q:
        #     smesters += 1
        #     for _ in range(len(q))
        #       pre_crs = q.popleft()
        #       completed += 1

        #       for nxt_crs in pre_to_course[pre_crs]:
        #           indegree[nxt_crs] -= 1

        #           if indegree[nxt_crs] == 0:
        #               q.append(nxt_crs)

        # return semesters if completed == numCourses else -1




        