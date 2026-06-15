class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l, r = 0, len(s)-1
        while l < r:
            temp_left = s[l]
            temp_right = s[r]
            s[l] = temp_right
            s[r] = temp_left
            l+=1
            r-=1