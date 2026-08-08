class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # store all arrival time in a list, 
        # then sort, earliest arriving monsters first
        # each monster has a deadline:arrival time, we can eliminate one monster per minute.
        # therefore eliminate the monster with the earliest arrival time first.
        # if one monsters arrval time <= current minutes(idx), mean we can not eliminate it, we already eliminated idx monsters return minutes(idx)
        #  if all monsters arrival time > current minutes(idx), we can eliminate all of them, return len of list of arrival time
        # Time:  O(nlogn) Space: O(n)

        arrival_times = []
        for d, s in zip(dist, speed):
            arrival = ceil(d/s)
            arrival_times.append(arrival)
        # Earliest arriving monsters first
        arrival_times.sort()

        for minute, arrival in enumerate(arrival_times):
            if arrival <= minute:
                return minute
        return len(arrival_times)
        