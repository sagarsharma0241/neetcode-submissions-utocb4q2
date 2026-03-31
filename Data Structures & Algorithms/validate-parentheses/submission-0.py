class Solution:
    def isValid(self, s: str) -> bool:
        closingDict = { ")": "(", "}": "{",  "]": "[" }
        stack = []
        for c in s : 
            if c in closingDict:
                if stack and stack[-1] == closingDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        print(stack)
        if stack :
            return False
        else:
            return True