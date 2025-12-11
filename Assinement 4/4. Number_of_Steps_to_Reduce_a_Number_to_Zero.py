class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Initialize the step counter
        steps = 0

        # Loop continues until the number is reduced to 0
        while num > 0:
            # Check if the number is even (num % 2 == 0)
            if num % 2 == 0:
                # Rule 1: If even, divide by 2
                num //= 2
            else:
                # Rule 2: If odd, subtract 1
                num -= 1

            # Increment the step counter for the operation just performed
            steps += 1

        return steps
