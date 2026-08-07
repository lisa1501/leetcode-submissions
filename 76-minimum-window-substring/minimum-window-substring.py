class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s = "ADOBeCOdEbANC", 
        #      012 3 456 789
        # t = "ABC" => a case =>"ADOBeC"
        # order s = "BDOAeCOdEBANC xyzxyx jdafjkdf", t = "ABC", order doens't matter "BDOAeC"
        # sliding window
        # t is sub str of s, we need all lelters and freq from t, get counter of t
        # get counter of s
        # "ABC"
        # res len +inf
        # res start store left index
        # loop thru s, intialize have =0
        # when s[i] in counter of t, and counter of s[i] == counter of s s[i]

        # when in counter of s , when we get 1 A, have+1

        # 1B, have+1
        # 1c have+1
        # have = 3  == counter of t this is means loop thru to here we get all letters and freq counter of t
        # when have same with len counter of t {a:1,b:1, c:2}
        # cur idx, l, r, len= r - l + 1 < res len, res len = r - l + 1 , res start is l
        # removing left idx letter from counter of s {A:0}
        # if left idx letter removing break codition:  counter of t this is means loop thru to here we get all letters and freq counter of t, have-=1
        # increament l point by 1 moving to right
        # return res start to res len
        # time O(n+m) loop throuhg s,t , n:len(s), m:len(t) space:O(k) kish the unique leeter s

        need = Counter(t)
        required = len(need)
        window = defaultdict(int)
        res_len= float('inf')
        res_start = 0
        have = 0
        l = 0 
        if len(s) < len(t):
            return ""
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1

            if ch in need  and need[ch] == window[ch]:
                have += 1

            while have == required:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_start = l

                left_ch = s[l]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                l += 1
        
        if res_len == float('inf'):
            return ""
        return s[res_start: res_start + res_len]


