class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        prefix = [[0] * 26 for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(26):
                prefix[i + 1][j] = prefix[i][j]
            prefix[i + 1][ord(s[i]) - ord('a')] += 1
    
        result = []
        for left, right, k in queries:
            freq = [0] * 26
            for j in range(26):
                freq[j] = prefix[right + 1][j] - prefix[left][j]
            
            odd_count = sum(f % 2 for f in freq)
            
            if odd_count // 2 <= k:
                result.append(True)
            else:
                result.append(False)
                
        return result
        
#         def isPali(s: str, k: int) -> bool:
#             if len(s) % 2 == 0:
#                 odd_allowed = 2 * k 
#             else:
#                 odd_allowed = 2 * k + 1
            
#             counter = Counter(s)
            
#             count = 0
#             for k, v in counter.items():
#                 if v % 2 == 1:
#                     count += 1
#             if count > odd_allowed:
#                 return False
#             return True
        
#         res = []
#         for l, r, k in queries:
#             res.append(isPali(s[l:r+1], k))
            
#         return res