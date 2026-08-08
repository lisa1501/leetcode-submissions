class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #time: O(n), O(1)
        # Best value of values[i] + i
        best_i = values[0] + 0
        answer = float("-inf")

        for j in range(1, len(values)):
            # the sum of the values of the sightseeing spots, minus the distance between them.
            answer = max(answer,best_i + values[j] - j)
            # update best_i to max
            best_i = max(best_i,values[j] + j)
        return answer
        