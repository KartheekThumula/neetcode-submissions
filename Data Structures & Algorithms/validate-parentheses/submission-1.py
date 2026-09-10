class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        stack = []

        for ch in s:
            if ch not in parentheses:
                stack.append(ch)
                continue
            if not stack:
                return False
            openingBracket = stack.pop()

            if openingBracket != parentheses[ch]:
                return False
        
        return False if stack else True