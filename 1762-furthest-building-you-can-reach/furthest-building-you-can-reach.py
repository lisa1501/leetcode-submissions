class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # time: O(nlogk) space: O(k), k is ladders 
        heap = []
        for i in range(len(heights) - 1):
            if heights[i+1] > heights[i]:
                climbs = heights[i+1] - heights[i]
                heapq.heappush(heap, climbs)

                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)

                if bricks < 0:
                    return i
        return len(heights) - 1
        