class Solution:
    def isPalindrome(self, s: str) -> bool:
        # build new alphanum string + lowercase
        test_str = ""
        
        for char in s:
            if char.isalnum():
                test_str += char.lower()
        
        # now test reverse for easy check
        return test_str == test_str[::-1]