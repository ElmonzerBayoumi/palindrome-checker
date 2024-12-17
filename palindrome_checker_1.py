class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = str(x)[::-1]
        string_x = str(x)
        if string_x == reversed_num:
            return True
        else:
            return False

# Testing the function
solution = Solution()

# Example 1
x1 = 121
print("Input:", x1, "Output:", solution.isPalindrome(x1))  # Expected: True

# Example 2
x2 = -121
print("Input:", x2, "Output:", solution.isPalindrome(x2))  # Expected: False

# Example 3
x3 = 10
print("Input:", x3, "Output:", solution.isPalindrome(x3))  # Expected: False
