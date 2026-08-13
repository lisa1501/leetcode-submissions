class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # time:O(n) space:O(n)
        maxDeque = deque()   # decreasing
        minDeque = deque()   # increasing

        left = 0
        longest = 0

        for right in range(len(nums)):

            # Maintain decreasing deque (front = maximum)
            while maxDeque and nums[right] > maxDeque[-1]:
                maxDeque.pop()

            maxDeque.append(nums[right])

            # Maintain increasing deque (front = minimum)
            while minDeque and nums[right] < minDeque[-1]:
                minDeque.pop()

            minDeque.append(nums[right])

            # Window is invalid
            while maxDeque[0] - minDeque[0] > limit:

                if nums[left] == maxDeque[0]:
                    maxDeque.popleft()

                if nums[left] == minDeque[0]:
                    minDeque.popleft()

                left += 1

            longest = max(longest, right - left + 1)

        return longest