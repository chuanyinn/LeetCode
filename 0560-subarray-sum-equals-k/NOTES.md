1. dp technique. Running sum approach to iterate through the array once: keep track of how many ways it can accumulate to a certain prefix_sum, and if previously there was an array that makes up just the distance between the subarray sum and the target, then there is a valid subarray.
2. We iterate through the array once, maintaining a running sum of elements encountered so far (prefix_sum).
3. At each step, we check if `prefix_sum - k` exists in prefix_sum_count. If it does, it means there is a subarray whose sum is `k`, so we increment `total_subarrays` by the count of such subarrays found.
4. We update the `prefix_sum_count` dictionary with the current `prefix_sum`.
5. Since we want to consider all possible subarrays, should not sort the array, or use the sliding window approach.​
