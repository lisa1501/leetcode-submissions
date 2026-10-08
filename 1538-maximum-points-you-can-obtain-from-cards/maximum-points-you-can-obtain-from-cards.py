class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        window_size = n - k

        cur_window_sum = sum(cardPoints[:window_size])
        min_window_sum = cur_window_sum

        for i in range(window_size, n):
            cur_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, cur_window_sum)

        return total - min_window_sum

        