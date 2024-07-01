​Originally wanted to use set operation keyed by the first letter, but for palindrome cannot just look at the first letter, but instead the whole string, so minimum complexity is at least O(n^2). Technique:
1. Iterate through each character in the string. For each character, consider it as the center of an odd-length palindrome.
2. Also, consider each pair of consecutive characters as the center of an even-length palindrome.
3. Expand around each center, counting palindromic substrings.

Note: write it in functions to implement odd and even by matching and unmatching indices.
