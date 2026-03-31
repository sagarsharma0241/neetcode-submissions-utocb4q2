class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def backTrack(open, closed):
            if n == open == closed:
                res.append("".join(stack))
                return 
            
            if open < n:
                stack.append("(")
                backTrack(open+1, closed)
                stack.pop()
            
            if closed < open:
                stack.append(")")
                backTrack(open, closed+1)
                stack.pop()
        backTrack(0,0)

        return res

        