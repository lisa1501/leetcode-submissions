class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # time : Time: O(V*V+ E + Q) Space: O(V*V + E) V:num of courses, E:num of prerequisites, Q:num of queries
        
        pre_to_crs = defaultdict(list)
        count_pres = [0] * numCourses

        for pre, crs in prerequisites:
            pre_to_crs[pre].append(crs)
            count_pres[crs] += 1

        q = deque()
        for crs in range(numCourses):
            if count_pres[crs] == 0:
                q.append(crs)

        prereq = [set() for _ in range(numCourses)]
        
        while q:
            pre_crs = q.popleft()
            
            for nxt_crs in pre_to_crs[pre_crs]: #O(V)
                # course is a direct prerequisite of nxt
                prereq[nxt_crs].add(pre_crs)
                # All prerequisites of course
                # are also prerequisites of nxt
                prereq[nxt_crs].update(prereq[pre_crs]) #O(V)

                count_pres[nxt_crs] -= 1

                if count_pres[nxt_crs] == 0:
                    q.append(nxt_crs)

        # Answer queries
        result = []
        for pre, crs in queries:
            result.append(pre in prereq[crs])
        return result