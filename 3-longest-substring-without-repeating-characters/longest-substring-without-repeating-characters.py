class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            cur_chr = s[right]
            while cur_chr in seen:
                seen.remove(s[left])
                left += 1

            seen.add(cur_chr)
            longest = max(longest, right-left+1)

        return longest 