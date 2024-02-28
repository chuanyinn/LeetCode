class Solution:
    def countLetters(self, s: str) -> int:
        res = 1
        cnt, l = 1, s[0]
        for i in range(1, len(s)):
            if s[i] == l:
                cnt += 1
            else:
                l = s[i]
                cnt = 1
            res += cnt

        return res