​Initial logic errror for accumulate result string as we go and compare that with newly absorbed string. But this greedy approach won't work if there are further away letters that causes smaller lexicographical string. Instead, stack-based approach:
1. Count the frequency of each character in the string.
1. Iterate through the string, and for each character:
  - Skip the character if it is already in the result.
  - While the character at the top of the stack is greater than the current character and appears later in the string, pop the stack.
  - Push the current character to the stack.
1. Join the stack to form the result string.
