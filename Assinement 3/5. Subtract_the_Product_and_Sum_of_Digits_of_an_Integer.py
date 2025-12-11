class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Initialize the product (P) to 1, as multiplying by 1 does not change the result.
        product_of_digits = 1

        # Initialize the sum (S) to 0, as adding 0 does not change the result.
        sum_of_digits = 0

        # Use a temporary variable to perform the digit extraction without modifying 'n'.
        temp_n = n

        # Loop continues as long as there are digits left in the number.
        while temp_n > 0:
            # 1. Extract the last digit:
            # The modulo operator (%) gives the remainder when dividing by 10.
            digit = temp_n % 10

            # 2. Update the product and sum:
            product_of_digits *= digit
            sum_of_digits += digit

            # 3. Prepare for the next digit:
            # Integer division (//) removes the last digit.
            temp_n //= 10

        # 4. Return the required result: Product - Sum
        return product_of_digits - sum_of_digits
