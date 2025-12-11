from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 1. Initialize a frequency array (count) for numbers 0 through 100.
        # Max value is 100, so array size 101 is sufficient (index 0 to 100).
        max_val = 100
        count = [0] * (max_val + 1)

        # 2. Populate the frequency array.
        # count[x] will store how many times the number x appears in nums.
        for num in nums:
            count[num] += 1

        # 3. Modify the count array to store the cumulative sum (Prefix Sum).
        # count[x] will now store how many numbers are LESS THAN OR EQUAL TO x.
        # This is not what we want yet, but is a necessary intermediate step.
        # We modify it slightly in step 4.

        # Calculate the number of elements smaller than 'i'
        # 'smaller_count[i]' will be the total count of numbers in 'nums'
        # that are strictly less than 'i'.
        smaller_count = [0] * (max_val + 1)

        # smaller_count[0] is 0 (no non-negative numbers are smaller than 0)
        # smaller_count[i] = smaller_count[i-1] + count[i-1]
        for i in range(1, max_val + 1):
            # The count of numbers strictly smaller than 'i'
            # is the count of numbers smaller than or equal to 'i-1'.
            smaller_count[i] = smaller_count[i - 1] + count[i - 1]

        # 4. Construct the result array.
        result = []
        for num in nums:
            # The answer for nums[i] is simply the value stored in smaller_count[nums[i]].
            result.append(smaller_count[num])

        return result
