class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        seen = set()
        left = 0

        for right in range(n):
            if s[right] not in seen:
                seen.add(s[right])
                longest = max(longest, right - left + 1)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

                seen.add(s[right])

        return longest
        