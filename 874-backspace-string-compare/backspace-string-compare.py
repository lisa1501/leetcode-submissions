class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def helper(word):
            res = []
            i = 0
            while i < len(word):
                if word[i] != "#":
                    res.append(word[i])
                    i += 1
                else:
                    if res != []:
                        res.pop()
                    i += 1
            return "".join(res)


        return helper(s) == helper(t)

                
        

                
        