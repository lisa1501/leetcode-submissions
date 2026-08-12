class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for cnt, ch in [(a,'a'), (b,'b'), (c,'c')]:
            if cnt > 0:
                heap.append((-cnt,ch))

        heapq.heapify(heap)

        result = []
        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == ch1:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                cnt2 += 1

                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))
                heapq.heappush(heap, (cnt1, ch1))
                
            else:
                result.append(ch1)
                cnt1 += 1

                if cnt1 < 0:
                    heapq.heappush(heap, (cnt1, ch1))
        return "".join(result)
        