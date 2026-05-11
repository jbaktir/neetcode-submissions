class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {"}":"{", "]":"[", ")":"("}
        for i in s:
            if i in closetoopen:
                if stack and closetoopen[i] == stack[-1]:
                    stack.pop()
                else: 
                    return False

            else:
                stack.append(i)
        if stack:
            return False
        return True
                