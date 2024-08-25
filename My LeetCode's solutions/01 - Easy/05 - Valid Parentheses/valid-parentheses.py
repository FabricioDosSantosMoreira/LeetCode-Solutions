from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 > 0: # if 's' is odd then 's' isn't valid
            return False

        stack: List[str] = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif len(stack) == 0:
                    return False
            else:
                if char.replace(")", "(").replace("]", "[").replace("}", "{") == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        
        return True if len(stack) == 0 else False


solution = Solution()


s: str = "()"
answer = solution.isValid(s=s)
print(f"return: {answer}")


s: str = "()[]{}"
answer = solution.isValid(s=s)
print(f"return: {answer}")


s: str = "(]"
answer = solution.isValid(s=s)
print(f"return: {answer}")


s: str = "([])"
answer = solution.isValid(s=s)
print(f"return: {answer}")


s: str = "(("
answer = solution.isValid(s=s)
print(f"return: {answer}")


s: str = "(){}}{"
answer = solution.isValid(s=s)
print(f"return: {answer}")


s: str = "(([]){})"
answer = solution.isValid(s=s)
print(f"return: {answer}")


s: str = "[({(())}[()])]"
answer = solution.isValid(s=s)
print(f"return: {answer}")


s: str = "([}}])"
answer = solution.isValid(s=s)
print(f"return: {answer}")
