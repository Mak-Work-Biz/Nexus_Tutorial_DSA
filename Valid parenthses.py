class Solution:
    def isValid(self, s: str) -> bool:
        pare = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in pare.values():
                stack.append(i)
            else:
                if not stack or stack[-1] != pare[i]:
                    return False
                stack.pop()

        return not stack
