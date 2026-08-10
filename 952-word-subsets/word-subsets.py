class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Global frequency requirement
        required = [0] * 26

        # Build requirements from words2
        for word in words2:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            # Take maximum requirement for each character
            for i in range(26):
                required[i] = max(required[i], count[i])

        res = []

        # Check every word in words1
        for word in words1:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            valid = True
            for i in range(26):
                if count[i] < required[i]:
                    valid = False
                    break

            if valid:
                res.append(word)

        return res
        