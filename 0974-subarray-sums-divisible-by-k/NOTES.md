Track the prefix sums ending at each index, instead of individual elements, and modulus + a hashmap to count the oc​curence of the remainders. If at two different points of the array we see the same remainder for the prefix sum, then the subarray between them is divisible by `k`.

Prefix Sum and Modulus:
- Compute the prefix sum as we iterate through the array.
- Calculate the remainder of the prefix sum when divided by `k`.
  
Using a Hashmap:
- Use a hashmap to count the occurrences of each remainder.
- If the same remainder appears again, it means the subarray between these two indices has a sum that is divisible by `k`.
