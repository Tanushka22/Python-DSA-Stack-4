class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = []

        for i in s:
            if i=='(' or i==')':
                stack.append(i)
                if stack[-1]==')' and stack[-2]=='(':
                    stack.pop()
                    stack.pop()
                    res.append(len(stack)+1)

        if len(res)==0:
            return 0
        else:
            return max(res)
