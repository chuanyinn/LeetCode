1. Recursion. Base case is `not node`. Current node catch False if not `lower <= node.val <= upper`. Recursive case checks the validity of the current node and recursively checks the left and right subtrees with updated bounds.
2. A better way to handle all single-leg cases at once without enumerating them is to just set bounds.
3. Note that Leetcode doesn't let you do recursion without naming a function inside the main function.
