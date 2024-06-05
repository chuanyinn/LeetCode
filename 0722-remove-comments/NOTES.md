Initialize Variables:
1. A flag to indicate if we are inside a block comment.
1. A list to store the current line being constructed.
1. A list to store the final output.

Iterate Through Each Line:
1. If inside a block comment, search for the end of the block comment (*/).
1. If not inside a block comment, search for the start of line (//) and block comments (/*).
1. Construct the line by appending characters that are not part of a comment.

Edge Cases:
1. Handle lines that are entirely within a block comment.
1. Ensure lines that become empty after comment removal are not added to the final output.​
