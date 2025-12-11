class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Initialize the result accumulator for the bitwise XOR operation.
        # The XOR identity element is 0, as any number XOR 0 is the number itself.
        result = 0

        # We need to generate 'n' elements, corresponding to i from 0 up to n-1.
        for i in range(n):
            # 1. Calculate the current element nums[i] = start + 2 * i
            current_num = start + 2 * i

            # 2. Update the result using the bitwise XOR operator (^).
            # result = result ^ current_num
            result ^= current_num

        return result
