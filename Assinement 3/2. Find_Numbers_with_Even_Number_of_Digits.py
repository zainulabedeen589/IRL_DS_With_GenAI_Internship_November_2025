from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Given an array of integers, return how many of them contain
        an even number of digits.
        """
        count = 0

        for num in nums:
            # --- Method 1: Convert to string and check length ---
            # This is often the simplest and most readable approach in Python.
            # 1. Convert the integer to its string representation.
            s = str(num)
            # 2. Check the length of the string (which is the number of digits).
            # 3. Use the modulo operator (%) to check if the length is even.
            if len(s) % 2 == 0:
                count += 1

            # --- Alternative Method 2: Mathematical approach (using log10 or division) ---
            # This avoids string conversion but is slightly more complex.

            # digits = 0
            # if num == 0:
            #     digits = 1
            # else:
            #     # For a positive integer 'num', the number of digits is
            #     # floor(log10(num)) + 1.
            #     # We can compute this manually using successive division by 10.
            #     digits = 0
            #     temp_num = num
            #     while temp_num > 0:
            #         temp_num //= 10  # Integer division
            #         digits += 1

            # if digits % 2 == 0:
            #     count += 1

        return count
