class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_count = Counter(s)
        
        # Stack to keep the result characters
        stack = []
        # Set to keep track of characters already in stack
        in_stack = set()
        
        for c in s:
            char_count[c] -= 1
            
            if c in in_stack:
                continue
            
            # Remove characters that are greater than current character and can be found later
            while stack and stack[-1] > c and char_count[stack[-1]] > 0:
                removed_char = stack.pop()
                in_stack.remove(removed_char)
            
            stack.append(c)
            in_stack.add(c)
        
        return ''.join(stack)
        
        
#         cur_str = ''
#         cur_set = set(cur_str)

#         for c in s:
#             if c in cur_set:
#                 temp_str = cur_str.replace(c, '')
#                 temp_str += c
#                 if temp_str < cur_str:
#                     cur_str = temp_str
#             else:
#                 cur_set.add(c)
#                 cur_str += c

#             print(cur_str)

#         return cur_str