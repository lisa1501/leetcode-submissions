class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longest(target):
            left = 0
            changes = 0
            ans = 0

            for right in range(len(answerKey)):
                if answerKey[right] != target:
                    changes += 1

                while changes > k:
                    if answerKey[left] != target:
                        changes -= 1

                    left += 1

                ans = max(ans, right - left + 1)

            return ans

        return max(longest('T'), longest('F'))
        