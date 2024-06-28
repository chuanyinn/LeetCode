Stack 
1. O(n) operation. Basically keep on appending result, and if the current operation is `*` or `/` we apply the operation immediately by replacing the last element in stack, but if the current operation is `+` or `-` we append the number.
2. Note that there's a one-cycle offset between the character read and the operation, so that when we read in the operation, the last element in stack is correctly storing the number to apply the operation to.
3. Eventually sum all the elements in stack together, which can be positive or negative.
4. "Truncating towards zero" is different for positive and negative numbers.
5. Initialization - ​current number is 0 because turning string into multi-digit integer, current operation is `+` because it's how we sum up everything too.
