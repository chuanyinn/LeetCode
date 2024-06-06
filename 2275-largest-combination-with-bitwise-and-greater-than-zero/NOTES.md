Optimizing with Bit Positions: Instead of checking all subsets directly, which is computationally expensive, we can focus on bit positions:
- For each bit position, count how many numbers have 1 at that bit position.
- The largest subset will be determined by the most frequent bit position with 1 across all numbers.

​We want max_bits instead of min_bits because it's okay if all leading digits are zero, so long as one of them is not zero.
