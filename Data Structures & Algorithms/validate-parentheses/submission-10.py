class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False

                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False

            
        return len(stack) == 0

        