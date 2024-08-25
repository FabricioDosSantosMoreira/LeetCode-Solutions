class Solution:
    def isPalindrome(self, x: int) -> bool:

        # NOTE: Time Complexity = O(k)
        # 'k' is the number of digits in the integer 'x'
        left = str(x)
        right = str(x)[: : -1]

        if left == right:
            return True
        return False


solution = Solution()


x: int = 121
answer = solution.isPalindrome(x=x)
print(f"return: {answer}")


x: int = -121
answer = solution.isPalindrome(x=x)
print(f"return: {answer}")


x: int = 10
answer = solution.isPalindrome(x=x)
print(f"return: {answer}")
