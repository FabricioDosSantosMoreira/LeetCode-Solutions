from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:

        # NOTE: Time Complexity = O(n)
        # 'n' is the length of the input string 's'
        ROMANS: Dict[str, int] = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        used_next: bool = False
        integer: int = 0

        for i in range(len(s)):
            if used_next:
                used_next = False
            else:
                value = ROMANS[s[i]]
                try:
                    next_value = ROMANS[s[i + 1]]
                except Exception as exc:
                    next_value = 0

                if value in [1, 10, 100] and next_value > value:
                    integer += next_value - value
                    used_next = True
                else:
                    integer += value
            
        return integer


solution = Solution()


s: str = "III" # 3
answer = solution.romanToInt(s=s)
print(f"return: {answer}")


s: str = "LVIII" # 58
answer = solution.romanToInt(s=s)
print(f"return: {answer}")


s: str = "MCMXCIV" # 1994
answer = solution.romanToInt(s=s)
print(f"return: {answer}")


s: str = "DCXXI" # 621
answer = solution.romanToInt(s=s)
print(f"return: {answer}")


s: str = "MDCXCV" # 1695
answer = solution.romanToInt(s=s)
print(f"return: {answer}")


s: str = "D" # 500
answer = solution.romanToInt(s=s)
print(f"return: {answer}")
