Initially thinking of half-baked heqpq, then recursion with trinomial trees, but this become cumbersome. Best approach is a greedy algorithm with max_heap (frequency inverted), so we always pick the most abundant character,
1. Create a Max-Heap: Use a max-heap (priority queue) to always select the character with the highest remaining count. This ensures we are always using the most available character as long as it doesn't violate the constraints.
1. Construct the String: At each step, select the character with the highest count that can be added without forming "aaa", "bbb", or "ccc". If this character can't be used due to the constraints, use the next most frequent character.
1. Alternate Choices: If we can't use the most frequent character, we need to use the second most frequent character to keep the string "happy". After using the second character, re-evaluate the counts and push the characters back into the heap.
1. Edge Cases: Handle edge cases where it's not possible to form a longer string without violating the constraints.
​
