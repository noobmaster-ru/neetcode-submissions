class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ["(", "{", "["]
        closed = [")", "}", "]"]
        pairs = ["()", "{}", "[]"]
        for char in s:  
            if char in closed and len(stack) == 0:
                return False
            if char in opens:
                stack.append(char)
            elif stack[-1] + char in pairs:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False       