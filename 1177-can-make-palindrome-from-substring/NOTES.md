TLE using `Counter` on each individual substring. Since lots of queries on different substrings of a given string, it makes sense to assemble a grid (prefix frequency arrays) that saves info about letters...

Handle Queries Efficiently:
- We need to process multiple queries efficiently.
- Use prefix frequency arrays to quickly calculate the frequency of each character in any substring.​

Understand Palindrome Properties:
- A palindrome reads the same forwards and backwards.
- For a string to be rearranged into a palindrome:
- If its length is even, all characters must appear an even number of times.
- If its length is odd, exactly one character can appear an odd number of times (the center character), while all others must appear an even number of times.
