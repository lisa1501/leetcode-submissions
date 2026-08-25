class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append([target, time])

        info = float('inf')
        times = [info] * (n+1)
        times[k] = 0

        heap = [(0,k)]

        while heap:
            send_time, source = heapq.heappop(heap)

            if send_time > times[source]:
                continue

            for target, need_time in graph[source]:
                new_time = send_time + need_time
                if new_time < times[target]:
                    times[target] = new_time
                    heapq.heappush(heap, (new_time, target))

        ans = max(times[1:])

        if ans != info:
            return ans
        return -1
        