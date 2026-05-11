class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sdict = {"}":"{", "]":"[", ")":"("}
        for i in s:
            if i in sdict:
                last = stack.pop() if stack else '#'
                if last != sdict[i]:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True