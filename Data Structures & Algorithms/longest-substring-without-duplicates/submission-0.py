class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for l in range(len(s)):
            seen = set()
            for r in range(l, len(s)):
                if s[r] in seen:
                    break
                seen.add(s[r])

            res = max(res, len(seen))
        return res