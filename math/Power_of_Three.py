class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n < 1:
            return False
        
        max_power_three = 3**19

        if max_power_three%n == 0:
            return True
        else:
            return False
