from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        # digits_as_one_str = ''.join(str(n) for n in digits)
        # sum_of = str(int(digits_as_one_str) + 1)
        # digits = list(map(int, sum_of))
        # return digits

        digits = list(map(int, str(int(''.join(str(n) for n in digits)) + 1)))
        return digits

    
        # if digits[-1] < 9: 
        #     digits[-1] = digits[-1] + 1
        #     return digits   

        # size: int = len(digits)
        # index_to_change: int = 0
        # for i in range(len(digits) -1, -1, -1):
        #     if digits[i] < 9:
        #         size = len(digits) - i
        #         index_to_change = i
        #         break
        
        # value_as_str = str(digits[index_to_change] + 1)
        # if len(value_as_str) > 1:
        #     size += 1
        # temp_array = [0] * size
        # temp_array[0] = int(value_as_str[0])
        # digits[index_to_change :] = temp_array

        # return digits



        # for i in range(len(digits) - 1, -1, -1):
        #     if digits[i] < 9:  # Is this digit lower than 9? If so add 1 and return!
        #         digits[i] = digits[i] + 1
        #         return digits
        #     else:  # So the digit is 9? Then change it to 0 and keep looping
        #         digits[i] = 0

        # digits.insert(0, 1)  # Insert '1' at index '0'
        # return digits


solution = Solution()


digits: List[int] = [1,2,3]
answer = solution.plusOne(digits=digits)
print(f"return: {answer}")


digits: List[int] = [4, 3, 2, 1]
answer = solution.plusOne(digits=digits)
print(f"return: {answer}")


digits: List[int] = [9, 9]
answer = solution.plusOne(digits=digits)
print(f"return: {answer}")


digits: List[int] = [9, 8, 9, 9]
answer = solution.plusOne(digits=digits)
print(f"return: {answer}")


digits: List[int] = [9]
answer = solution.plusOne(digits=digits)
print(f"return: {answer}")


digits: List[int] = [0]
answer = solution.plusOne(digits=digits)
print(f"return: {answer}")
