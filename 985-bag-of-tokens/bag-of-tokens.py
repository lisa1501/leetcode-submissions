class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        score = 0
        ans = 0

        while left <= right:

            # Option 1: play face up
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                ans = max(ans, score)
                left += 1

            # Option 2: play face down
            elif score > 0 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1

            else:
                break

        return ans
        