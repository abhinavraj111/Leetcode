class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        # Find the maximum number of candies any kid currently has
        max_candies = max(candies)
        
        # Check if each kid can have the greatest number of candies after getting the extra candies
        result = [(candy + extraCandies) >= max_candies for candy in candies]
        
        return result

# Example usage:
solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))  # Output: [True, True, True, False, True]
print(solution.kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [True, False, False, False, False]
print(solution.kidsWithCandies([12, 1, 12], 10))    # Output: [True, False, True]
