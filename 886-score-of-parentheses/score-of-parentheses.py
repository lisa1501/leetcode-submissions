class Solution:
    def scoreOfParentheses(self, s: str) -> int:
# "()" has score 1.
# Input: s = "()" => Output: 1

# AB has score A + B, where A and B are balanced parentheses strings.
# Input: s = "()()" Output: 2

# (A) has score 2 * A, where A is a balanced parentheses string.
# Input: s = "(())" Output: 2

# "()" has score 1.
# hm ={")" :"("}

# s = "(())"
# loop thru s
# stack [(,(]
# count = score * len(stack)


# s = "()()"
# stack = [(]
# time: O(n) space: O(n)

# "((()))()()"
# [()(()) ]    1 * 2**(len(stack) - 1)


# (()) nested level: 1, score: 2
# ((()())) 2 -> 4
# (((( )))) 3 -> 8

# "((()))()()"

        ans = 0
        opening = 0

        for i in range(len(s)):
            cur_ch = s[i]
            if cur_ch == ")":
                opening -= 1  
                if s[i-1] == "(":
                    ans += 2**(opening)    
            else:
                opening += 1

        return ans 




        