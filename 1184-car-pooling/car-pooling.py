class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        current = 0

        for i in range(1001):
            current += diff[i]

            if current > capacity:
                return False

        return True
        