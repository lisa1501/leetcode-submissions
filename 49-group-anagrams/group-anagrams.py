class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for i in range(len(strs)):
            s = strs[i]
            arr = [0] * 26
            for j in range(len(s)):
                ch = s[j]
                idx = ord(ch) - ord('a')
                arr[idx] += 1
            freq[tuple(arr)].append(s)

        return [val for val in freq.values()]
        