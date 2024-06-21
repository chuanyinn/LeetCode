class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # approach 2: store the counter string of each of the alphabet as the key. 
        # O(N * K)
        res: DefaultDict[int, List[str]] = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[(tuple(count))].append(s)
        
        return res.values()
        
        