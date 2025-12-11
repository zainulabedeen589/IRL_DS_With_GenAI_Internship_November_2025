from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Use Counter to get the frequency of each number
        counts = Counter(nums)
        good_pairs_count = 0

        # Iterate through the frequencies (k) of each unique number
        for count in counts.values():
            # If a number appears 'count' times, it forms 'count * (count - 1) / 2' pairs.
            # Example: If a number appears 4 times, it forms 4 * 3 / 2 = 6 pairs.
            if count >= 2:
                # Integer division // is used since the result is guaranteed to be an integer.
                pairs = count * (count - 1) // 2
                good_pairs_count += pairs

        return good_pairs_count
