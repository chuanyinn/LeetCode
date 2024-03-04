class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # at most len(num1) + len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        result = [0] * (len(num1) + len(num2))
        for i, a in enumerate(num1):
            for j, b in enumerate(num2):
                # careful, take into account previously added number
                result[i+j] += int(a) * int(b)
                result[i+j+1] += result[i+j] // 10
                result[i+j] %= 10

        # removing leading zeros from the result, currently at the end
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # convert the result list to a string, reverse it back
        return ''.join(str(p) for p in result[::-1])

