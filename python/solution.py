# Copy/paste template from LeetCode below
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            print(s[left] + " == " + s[right])
            while left < right and not self.isAlphanum(s[left]):
                left += 1
            
            while right > left and not self.isAlphanum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        
        return True

    
    def isAlphanum(self, character: str) -> bool:
        return (
            ord("A") <= ord(character) <= ord("Z") or
            ord("a") <= ord(character) <= ord("z") or
            ord("0") <= ord(character) <= ord("9")
        )

# After copy/pasting the template from LeetCode, uncomment the following to start testing.
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))