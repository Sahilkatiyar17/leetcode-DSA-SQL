class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':  # Fixed condition
                stack.append(s[i])
            else:
                if not stack:  # Check to avoid accessing an empty stack
                    return False
                if s[i] == ")" and stack[-1] == '(':
                    stack.pop()
                elif s[i] == "]" and stack[-1] == '[':
                    stack.pop()
                elif s[i] == "}" and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return not stack  # Ensure stack is empty at the end


        