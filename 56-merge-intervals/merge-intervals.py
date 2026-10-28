class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sorted_intervals = sorted(intervals)

        merged_intervals = []

        for interval in sorted_intervals:
            start = interval[0]
            end = interval[1]

            if not merged_intervals or start > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

        return merged_intervals
        
        