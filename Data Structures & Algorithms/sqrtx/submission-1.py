class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            mid = (l+r) // 2
            if mid**2 > x:
                r = mid - 1
            elif mid**2 < x:
                l = mid + 1
                # keep updating res with the lowest mid to return once loop ends
                res = mid
            else:
                # perfect match
                return mid
        return res