class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        def helper(s: str) -> str:
            res = ''
            i = 0
            while i < len(s):
                count = 1
                while i + count < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                res += str(count) + s[i]
                i += 1
            return res
        
        current = '1'
        for _ in range(1, n):
            current = helper(current)
            
        return current