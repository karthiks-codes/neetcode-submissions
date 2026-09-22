class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        o = 0
        c = 0

        def traverse(o: int, c: int):
            if o == c == n:
                res.append("".join(stack))
                return

            if o < n:
                stack.append("(")
                traverse(o + 1, c)
                stack.pop()

            if o > c:
                stack.append(")")
                traverse(o, c + 1)
                stack.pop()

        traverse(o, c)
        return res

        