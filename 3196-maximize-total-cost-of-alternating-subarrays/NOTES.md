I tried dp (two arrays) but didn't get it working. Here is a very efficient way..
- An element can always be positive by first term that starts a subarray. But to be negative it needs to be placed the second...
- This is essentially 2D dp array, but more efficient because takes up less space.

Implementation
1. Collect a size 2 tuple and update it​ as we move across the list
2. First term `a` represents if we start fresh by adding a bin right before the index `i`. That's why it's initialized as `nums[0]` and updates by simple addition of the maximum of the two previous tuple.
3. Second term `b` represents if we keep previous binning. Question is why can we just update with `-nums[i]`? What if it's at an even number? The insight is that this would be the same as starting fresh...
