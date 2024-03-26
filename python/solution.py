# Copy/paste template from LeetCode below
class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_list = [char.lower() for char in s if char.isalnum()]
        
        for index in range(len(normalized_list) // 2):
            if normalized_list[index] != normalized_list[~index]:
                return False
        
        return True

# After copy/pasting the template from LeetCode, uncomment the following to start testing.
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("rat"))