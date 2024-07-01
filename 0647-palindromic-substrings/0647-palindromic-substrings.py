class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp expanding around the center
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
            return count
        
        total_count = 0
        
        for i in range(len(s)):
            # odd
            total_count += expand_around_center(i, i)
            # even
            total_count += expand_around_center(i, i+1)
            
        return total_count