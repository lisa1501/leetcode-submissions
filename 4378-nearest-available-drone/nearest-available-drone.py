class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        minDistance = float('inf')
        result = None

        for i in range(len(drones)):
            x = drones[i][0]
            y = drones[i][1]
            z = drones[i][2]
            currentDistance = abs(x - target[0]) + abs(y - target[1])
            if currentDistance >= minDistance or currentDistance > z:
                continue
            else:
                minDistance = currentDistance
                result = i

        if result == None:
            return -1
        else:
            return result

        