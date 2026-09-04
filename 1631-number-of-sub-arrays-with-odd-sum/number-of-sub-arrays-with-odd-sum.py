class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = 0
        prefix_sum = 0
        count_odd = 0
        count_even = 1
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                count = (count + count_odd) % (10**9 + 7)
                count_even += 1
            else:
                count = (count + count_even) % (10**9 + 7)
                count_odd += 1

        return count
        