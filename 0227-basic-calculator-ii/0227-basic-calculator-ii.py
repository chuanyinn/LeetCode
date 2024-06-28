class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operation = '+'

        def apply_operation(operation, current_number):
            if operation == '+':
                stack.append(current_number)
            elif operation == '-':
                stack.append(-current_number)
            elif operation == '*':
                stack.append(stack.pop() * current_number)
            elif operation == '/':
                # Integer division truncating towards zero
                last = stack.pop()
                if last < 0:
                    stack.append(-(-last // current_number))
                else:
                    stack.append(last // current_number)

        # Iterate through each character in the string
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            if char in "+-*/" or i == len(s) - 1:
                apply_operation(operation, current_number)
                current_number = 0
                operation = char
        print(stack)
        # Sum up all values in the stack
        return sum(stack)
        
        
        
#         l = re.split(r'[\+\-\*/]', s)
#         nums = [int(c) for c in l]
#         ops = []
#         for c in s:
#             if c in ['+', '-', '*', '/']:
#                 ops.append(c)
        
#         print(nums, ops)
#         for i, op in enumerate(ops):
#             if op == '*':
#                 a, b = nums[i], nums[i+1]
#                 nums.pop(i+1)
#                 nums[i] = a * b
#             elif op == '/':
#                 a, b = nums[i], nums[i+1]
#                 nums.pop(i+1)
#                 nums[i] = a // b
        
#         ops = [op for op in ops if op in ['+', '-']]
        
#         res = nums[0]
#         if not ops:
#             return res
        
#         for i, op in enumerate(ops):
#             if op == '+':
#                 res += nums[i+1]
#             else:
#                 res -= nums[i+1]
        
#         return res