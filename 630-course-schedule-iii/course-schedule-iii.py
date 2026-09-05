class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 1. Sort by deadline
        courses.sort(key=lambda x: x[1])

        max_heap = []
        total_time = 0

        # 2. Try to take every course
        for duration, deadline in courses:

            total_time += duration

            # Python heap is min heap
            # Store negative values for max heap behavior
            heapq.heappush(max_heap, -duration)

            # 3. If deadline exceeded,
            # remove the longest course
            if total_time > deadline:

                longest = -heapq.heappop(max_heap)

                total_time -= longest

        return len(max_heap)
        