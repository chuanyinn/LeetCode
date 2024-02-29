class Solution:
    def toHexspeak(self, num: str) -> str:
        res = []
        hex_str = hex(int(num))[2:].upper()
        hex_str = hex_str.replace('1', 'I')
        hex_str = hex_str.replace('0', 'O')
        for h in hex_str:
            if h not in "ABCDEFIO":
                return "ERROR"
        return hex_str