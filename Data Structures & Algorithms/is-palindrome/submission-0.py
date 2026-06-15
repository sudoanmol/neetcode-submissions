class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char.lower())
        
        dup = arr.copy()

        l, r = 0, len(dup)-1
        while l < r:
            temp_left = dup[l]
            temp_right = dup[r]
            dup[l] = temp_right
            dup[r] = temp_left
            l+=1
            r-=1
        
        if arr == dup:
            return True
        else:
            return False