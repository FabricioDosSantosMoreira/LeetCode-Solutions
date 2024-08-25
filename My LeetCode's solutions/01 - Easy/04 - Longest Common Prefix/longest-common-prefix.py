from typing import List
import numpy as np


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # NOTE: Time Complexity = O(L * n)
        # 'L' is the length of the longest string in the list
        # 'n' is the number of strings in the list.
        prefix: str = ""
        for i in range(len(max(strs))):
            y_chars: List[str] = []
            for y in range(len(strs)):      
                try:
                    y_chars.append(strs[y][i])
                except IndexError as exc:
                    return prefix

            if all(element == y_chars[0] for element in y_chars):
                prefix += y_chars[0]
            else:
                break

        return prefix


solution = Solution()


strs = ["cir","car"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = ["abab","aba","abc"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = ["aaa","aa","aaa"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = ["reflower","flow","flight"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = ["flower", "flower", "flower", "flower"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = ["flower", "flow", "flight"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = ["dog","racecar","car"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = ["a"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = ["ab", "a"]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")


strs = [""]
answer = solution.longestCommonPrefix(strs=strs)
print(f"return: {answer}")
