class Solution:
    def isValid(self, s: str) -> bool:
        collect = {")":"(", "]":"[", "}":"{"}
        stack = []

        for p in s:
            if p not in collect:
                stack.append(p)

            else:
                if stack and stack[-1] == collect[p]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    

        